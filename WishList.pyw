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

    path = './Wishes/'

    fileName = str(wishList.get(tkinter.ACTIVE).split(' ')[2]) + '.txt'

    newInfo = ReadFile(path, fileName)

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

    path = './Wishes/'

    fileName = str(wishList.get(tkinter.ACTIVE).split(' ')[2]) + '.txt'

    newInfos = ReadFile(path, fileName).split(',')

    wishData = {}

    wishData["Username"] = newInfos[0]
    wishData["Type"] = newInfos[1]
    wishData["Amount"] = newInfos[2].split(' ')[0].split('.')[0]



    if(wishData["Type"] == 'sell'):

        path = './'
        fileName = 'Gold.txt'

        goldInfo = ReadFile(path, fileName)

        cost = int(wishData["Amount"]) * int(95)

        if(int(goldInfo) < cost):
            print('rejected, not enough gold in bank')
            return Reject()

        path = './Users/'
        fileName = wishData["Username"] + '.txt'

        newInfo = ReadFile(path, fileName).split(',')

        userData = {}

        userData["Username"] = newInfo[0]
        userData["Password"] = newInfo[1]
        userData["Email"] = newInfo[2]
        userData["GM"] = newInfo[3]
        userData["Rank"] = newInfo[4]
        userData["Balance"] = newInfo[5]

        newRank =  int(userData["Rank"]) #+ (int(wishData["Amount"]))

        newBalance = int(userData["Balance"]) - (int(wishData["Amount"]) * 1000)

        newInfo = userData["Username"] + ',' + userData["Password"]  + ',' + userData["Email"] + ',' + userData["GM"] + ',' + str(newRank) + ',' + str(newBalance)

        WriteFile(path, fileName, newInfo)

        

        newInfo = str(int(goldInfo) - ((int(wishData["Amount"])) * 95))

        path = './'
        fileName = 'Gold.txt'

        WriteFile(path, fileName, newInfo)

        

    if(wishData["Type"] == 'buy'):
        
        path = './Users/'
        fileName = wishData["Username"] + '.txt'

        newInfo = ReadFile(path, fileName).split(',')

        userData = {}

        userData["Username"] = newInfo[0]
        userData["Password"] = newInfo[1]
        userData["Email"] = newInfo[2]
        userData["GM"] = newInfo[3]
        userData["Rank"] = newInfo[4]
        userData["Balance"] = newInfo[5]

        newRank = int(userData["Rank"]) #+ (int(wishData["Amount"]))

        newBalance = int(userData["Balance"]) + (int(wishData["Amount"]) * 1000)

        newInfo = userData["Username"] + ',' + userData["Password"]  + ',' + userData["Email"] + ',' + userData["GM"] + ',' + str(newRank) + ',' + str(newBalance)

        WriteFile(path, fileName, newInfo)

        path = './'
        fileName = 'Gold.txt'

        goldInfo = ReadFile(path, fileName)

        newInfo = str(int(goldInfo) + ((int(wishData["Amount"])) * 105))

        WriteFile(path, fileName, newInfo)

    path = './Wishes/'
    fileName = str(wishList.get(tkinter.ACTIVE).split(' ')[2]) + '.txt'

    DeleteFile(path, fileName)

    UpdateWishList()

    logInfo = 'Wish confirmed: ' + wishData + ' new Guild Gold is: ' + GetGuildGold()

    LOG(logInfo)

    

def Reject():
    
    path = './Wishes/'

    fileName = str(wishList.get(tkinter.ACTIVE).split(' ')[2]) + '.txt'

    logInfo = 'Wish rejected! ' + ReadFile(path, fileName)

    LOG(logInfo)

    DeleteFile(path, fileName)

    UpdateWishList()

    
    

def UpdateWishList():
    
    path = './Wishes/'

    files = []

    

    for r,d,f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))


    wishList.delete(0, tkinter.END)
                
    order = 1
    for file in files:

        fileName = str(file).split('.')[1].split('/')[2] + '.txt'

        wishInfos = ReadFile(path, fileName).split(',')

        wishData = {}

        wishData["Username"] = wishInfos[0]
        wishData["Type"] = wishInfos[1]
        wishData["Amount"] = wishInfos[2]

        ListItem = str(order) + ')  ' + fileName.split('.')[0]
        
        wishList.insert(tkinter.END, ListItem)

        order += 1
        


       
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

