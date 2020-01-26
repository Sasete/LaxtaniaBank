import tkinter
from subprocess import Popen
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import sys
import socket
import time




def Open(path):
    Popen('py ' + path, shell = True)

def Close():
    sys.exit(0)

# This function reads from file
def ReadFile(m_path, m_fileName):
    filePathName = m_path + m_fileName

    m_file = open(filePathName, 'r')

    m_current = m_file.read()

    m_file.close()

    return m_current

def Error(errTitle, errString):
    messagebox.showerror(errTitle, errString)


def Info(errTitle, errString):
    messagebox.showinfo(errTitle, errString)



# This function creates empty file
def CreateFile(m_path, m_fileName):
    WriteFile(m_path, m_fileName, '')

    return

# This function deletes file
def DeleteFile(m_path, m_fileName):
    
    os.remove(m_path + m_fileName)


# This function writes into file with deleting previously info
def WriteFile(m_path, m_fileName, m_data):

    m_file = open(m_path + m_fileName, 'w')

    m_file.write(m_data)

    m_file.close()

    return


def GetTempData():

    path = './'
    fileName = 'temp.txt'
    
        
    newData = ReadFile(path, fileName).split(',')
        
    temp_info = {}

    temp_info["Username"] = newData[0]
    temp_info["Balance"] = newData[1]
    
    
    DeleteFile(path, fileName)

    return temp_info

userInfo = GetTempData()

def CreateTempData(data):
    
    CreateFile('./','temp.txt')
        
    WriteFile('./','temp.txt', data)

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

    
def SendCredit():


    

    targetUser = str(userList.get(tkinter.ACTIVE)).split(' ')[2]

    amount = E_amount


    if(int(amount.get()) <= 0):
        return Error('Error', 'No amount given!')

    data = 'SendCredit/' + userInfo["Username"] + ',' + str(E_amount.get()) + ',' + targetUser

    print(data)
    AskServer(data)


    Info('Success', 'Your credits successfully sent to player. Plase don\'t forget to get your service from him/her. ;)')



def UpdateUserList():

    
    users = str(AskServer('AskUsers/')).split(';')

    
    userList.delete(0, tkinter.END)
                
    order = 1
    for user in users:

        username = str(order) + ')  ' + user 
        
        userList.insert(tkinter.END, username)

        order += 1
        


        
main = tkinter.Tk()
main.title("Userlist")
main.resizable(False,False)

themeColor = "gray"
systemColor = "black"
userColor = "white"

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

userList = tkinter.Listbox(mainFrame, bg = themeColor, width = 60,font = 20, height = 20, yscrollcommand = scrollbar.set)
userList.pack()


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

E_amount = tkinter.StringVar()
E_amount.set('0')

EntryField = tkinter.Entry(midFrame, bg = themeColor, fg = userColor, font = 24, textvariable = E_amount, justify = tkinter.CENTER)
EntryField.pack(side = tkinter.TOP)


sendButton = tkinter.Button(midFrame, bg = themeColor, fg = systemColor, text = "Send", font = 24, width = 10, height = 2, command = SendCredit)
sendButton.pack(side = tkinter.BOTTOM)

def sendtkinter(event):
    SendCredit()

main.bind('<Return>', sendtkinter)


def refreshtkinter(event):
    UpdateUserList()

main.bind('r', refreshtkinter)


exitButton = tkinter.Button(bot_sideFrame, bg = themeColor, fg = systemColor, text = "Exit", font = 24, width = 10, height = 2, command = Close)
exitButton.pack(side = tkinter.BOTTOM)

updateButton = tkinter.Button(bot_sideFrame, bg = themeColor, fg = systemColor, text = "Update", font = 24, width =10, height = 2, command = UpdateUserList)
updateButton.pack(side = tkinter.BOTTOM)


host = "laxtaniabank.ddns.net"
port = 7676


bufferSize = 1024


UpdateUserList()

tkinter.mainloop()
