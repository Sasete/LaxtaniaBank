import tkinter
from subprocess import Popen
from tkinter import messagebox
from PIL import ImageTk, Image
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import sys
from datetime import datetime
import socket




host = "laxtaniabank.ddns.net"
port = 7676


bufferSize = 1024



def Error(errTitle, errString):
    messagebox.showerror(errTitle, errString)


def Info(errTitle, errString):
    messagebox.showinfo(errTitle, errString)

    
def AskServer(data):

    message = data
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((host,port))
    
        s.send( bytes(message, "utf-8") )



        message = s.recv(bufferSize)



        reply = format(message).split('\'')[1]


    
        print(reply)
    
        return reply

    except:
        return Error('Error Occured', 'Unkown error occured...')


def GetTempData():

    path = './'

    fileName = 'temp.txt'

    
    ReadFile(path, fileName)
    
    DeleteFile(path, fileName)

    return 1




def Open(path):
    Popen('Python ' + path, shell = True)

def Close():
    sys.exit(0)

# This function reads from file
def ReadFile(m_path, m_fileName):
    filePathName = m_path + m_fileName

    m_file = open(filePathName, 'r')

    m_current = m_file.read()

    m_file.close()

    return m_current



# This function creates empty file
def CreateFile(m_path, m_fileName):
    WriteFile(m_path, m_fileName, '')

    return

# This function deletes file
def DeleteFile(m_path, m_fileName):
    
    os.remove(m_path + m_fileName)


def CreateTempData(data):
    
    CreateFile('./','temp.txt')
        
    WriteFile('./','temp.txt', data)
    
# This function writes into file with deleting previously info
def WriteFile(m_path, m_fileName, m_data):

    m_file = open(m_path + m_fileName, 'w')

    m_file.write(m_data)

    m_file.close()

    return

def Details():

    path = 'Wishes'

    fileName = str(wishList.get(tkinter.ACTIVE).split(' ')[2])

    newInfo = AskServer('Details/' + path + ',' + fileName)

    CreateTempData(newInfo)

    Open('./WishDetail.pyw')

def LOG(m_input):
    info = ReadFile('./', 'Log.txt')


    info += m_input + '/' + str(datetime.now()) + '\n'

    WriteFile('./', 'Log.txt', info)
    

def GetGuildGold():

    path = './'

    fileName = 'Gold.txt'

    gold = ReadFile(path, fileName)

    return gold

def Confirm():

    
    fileName = str(wishList.get(tkinter.ACTIVE).split(' ')[2])

    response = AskServer('ConfirmWish/' + fileName)

    if(response == 'Success'):
        
        UpdateWishList()

        return 1

    else:

        message = response.split(',')

        Error(message[0], message[1])

        return 0
        

    

def Reject():
    
    
    fileName = str(wishList.get(tkinter.ACTIVE).split(' ')[2])

    AskServer('RejectWish/' + fileName)

    UpdateWishList()

    
    

def UpdateWishList():
    
    wishes = AskServer('AskWishes/').split(';')

    

    if(wishes[0] == 'Empty'):
        
        wishList.delete(0, tkinter.END)
        
        return 0

    else:


        wishList.delete(0, tkinter.END)
                
        order = 1
        for wish in wishes:

            wishInfos = wish.split(',')

            
            wishData = {}

            wishData["Username"] = wishInfos[0]
            wishData["Type"] = wishInfos[1]
            wishData["Amount"] = wishInfos[2]
            fileName = wishInfos[3]

            ListItem = str(order) + ')  ' + fileName.split('.')[0]
        
            wishList.insert(tkinter.END, ListItem)

            order += 1

        

GetTempData()
       
main = tkinter.Tk()
main.title("Wish List")
main.resizable(False,False)

themeColor = "gray"
systemColor = "black"
    

m_height = 400
m_width = 400


sideSpace = 50
topBottomSpace = 125


mainFrame = tkinter.Frame(main, bg = themeColor, height = m_height, width = m_width)
mainFrame.pack(side = tkinter.LEFT, fill = tkinter.Y)

titleFrame = tkinter.Frame(mainFrame, bg = themeColor, width = m_width, height = 30)
titleFrame.pack(side = tkinter.TOP, fill = tkinter.X)

#TODO Scrollbarın görüntüsü degistirilecek
scrollbar = tkinter.Scrollbar(mainFrame)
scrollbar.pack(side = tkinter.LEFT, fill = tkinter.Y)

wishList = tkinter.Listbox(mainFrame, bg = themeColor, width = 60,font = 20, height = 20, yscrollcommand = scrollbar.set)
wishList.pack()


s_height= 400
s_width = 200

sideFrame = tkinter.Frame(main, bg = themeColor, height = s_height, width = s_width)
sideFrame.pack(side = tkinter.RIGHT , fill = tkinter.Y)

divider = tkinter.Frame(main, bg = "black", height = s_height, width = 2)
divider.pack(side = tkinter.RIGHT, fill = tkinter.Y)



left_sideFrame = tkinter.Frame(sideFrame, bg = themeColor, height = s_height, width = sideSpace)
left_sideFrame.pack(side = tkinter.LEFT, fill = tkinter.Y)



right_sideFrame = tkinter.Frame(sideFrame, bg = themeColor, height = s_height, width = sideSpace)
right_sideFrame.pack(side = tkinter.RIGHT, fill = tkinter.Y)

mid_sideFrame = tkinter.Frame(sideFrame, bg = themeColor, height = s_height, width = s_width - 2 * sideSpace)
mid_sideFrame.pack(side = tkinter.RIGHT, fill = tkinter.Y)




top_sideFrame = tkinter.Frame(mid_sideFrame, bg = themeColor, height = topBottomSpace)
top_sideFrame.pack(side = tkinter.TOP, fill = tkinter.X)




bot_sideFrame = tkinter.Frame(mid_sideFrame, bg = themeColor, height = topBottomSpace)
bot_sideFrame.pack(side = tkinter.BOTTOM, fill = tkinter.X)

midFrame = tkinter.Frame(mid_sideFrame, bg = themeColor, height = topBottomSpace)
midFrame.pack(side = tkinter.TOP, fill = tkinter.X)


RejectButton = tkinter.Button(midFrame, bg = themeColor, fg = systemColor, text = "Reject", font = 24, width = 10, height = 2, command = Reject)
RejectButton.pack(side = tkinter.BOTTOM)

ConfirmButton = tkinter.Button(midFrame, bg = themeColor, fg = systemColor, text = "Confirm", font = 24, width = 10, height = 2, command = Confirm)
ConfirmButton.pack(side = tkinter.BOTTOM)

DetailsButton = tkinter.Button(midFrame, bg = themeColor, fg = systemColor, text = "Details", font = 24, width = 10, height = 2, command = Details)
DetailsButton.pack(side = tkinter.BOTTOM)

exitButton = tkinter.Button(bot_sideFrame, bg = themeColor, fg = systemColor, text = "Exit", font = 24, width = 10, height = 2, command = Close)
exitButton.pack(side = tkinter.BOTTOM)

updateButton = tkinter.Button(bot_sideFrame, bg = themeColor, fg = systemColor, text = "Update", font = 24, width =10, height = 2, command = UpdateWishList)
updateButton.pack(side = tkinter.BOTTOM)




UpdateWishList()

tkinter.mainloop()

