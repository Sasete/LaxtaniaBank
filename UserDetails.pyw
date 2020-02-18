import tkinter
from subprocess import Popen
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import sys
from datetime import datetime
import socket




host = "laxtaniabank.ddns.net"
port = 7676


bufferSize = 1024



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


 

# This function reads from file
def ReadFile(m_path, m_fileName):
    filePathName = m_path + m_fileName

    m_file = open(filePathName, 'r')

    m_current = m_file.read()

    m_file.close()

    return m_current

# This function writes into file with deleting previously info
def WriteFile(m_path, m_fileName, m_data):

    m_file = open(m_path + m_fileName, 'w')

    m_file.write(m_data)

    m_file.close()

    return


# This function deletes file
def DeleteFile(m_path, m_fileName):
    
    os.remove(m_path + m_fileName)


def Error(errTitle, errString):
    messagebox.showerror(errTitle, errString)



def GetTempData():

    path = './'
    fileName = 'temp.txt'
    
        
    newData = ReadFile(path, fileName).split(',')
        
    temp_info = {}

    temp_info["Username"] = newData[0]
    temp_info["Password"] = newData[1]
    temp_info["Email"] = newData[2]
    temp_info["GM"] = newData[3]
    temp_info["Rank"] = newData[4]
    temp_info["Balance"] = newData[5]
    
    
    DeleteFile(path, fileName)

    return temp_info

def SetRank():

    newRank = str(EntryField.get())

    newInfo = userData["Username"] + ',' + userData["Password"] + ',' + userData["Email"] + ',' + userData["GM"] + ',' + newRank + ',' + userData["Balance"]

    logInfo = 'Rank of ' + userData["Username"] + ' set to ' + newRank + '; ' + newInfo

    AskServer('SetRank/' + userData["Username"] + ';' + newInfo + ';' + logInfo)

    UpdatePage(userData["Username"])
    

def SetBalance():
    
    newBalance = str(EntryField.get())

    newInfo = userData["Username"] + ',' + userData["Password"] + ',' + userData["Email"] + ',' + userData["GM"] + ',' + userData["Rank"] + ',' + newBalance

    logInfo = 'Balance of ' + userData["Username"] + ' set to ' + userData["Rank"] + '; ' + newInfo
    
    AskServer('SetBalance/' + userData["Username"] + ';' + newInfo + ';' +logInfo)

    UpdatePage(userData["Username"])
    

def GetUserData(username):

    userInfo = AskServer('UserInfo/' + username)

    newData = userInfo.split(',')

    temp_info = {}

    temp_info["Username"] = newData[0]
    temp_info["Password"] = newData[1]
    temp_info["Email"] = newData[2]
    temp_info["GM"] = newData[3]
    temp_info["Rank"] = newData[4]
    temp_info["Balance"] = newData[5]

    return temp_info
    


def UpdatePage(username):

    user_data = GetUserData(username)

    usernameText = 'Username : ' + user_data["Username"]
    RankText = 'Rank : ' + user_data["Rank"]
    BalanceText = 'Balance : ' + user_data["Balance"] + ' £'


    usernameLabel.config(text = usernameText)
    rankLabel.config(text = RankText)
    balanceLabel.config(text = BalanceText)



userData = GetTempData()


main = tkinter.Tk()
main.title(userData["Username"])
main.resizable(False,False)


themeColor = "gray"
systemColor = "black"
userColor = "white"


topFrame = tkinter.Frame(main, bg = themeColor, width = 300, height = 200)
topFrame.pack(side = tkinter.TOP, fill = tkinter.X)

divider = tkinter.Frame(main, bg = systemColor, width = 300, height = 2)
divider.pack(side = tkinter.TOP, fill = tkinter.X)

mainFrame = tkinter.Frame(main, bg = themeColor, width = 300, height = 200)
mainFrame.pack(side = tkinter.TOP, fill = tkinter.X)

usernameText = 'Username : ' + userData["Username"]
RankText = 'Rank : ' + userData["Rank"]
BalanceText = 'Balance : ' + userData["Balance"] + ' £'

usernameLabel = tkinter.Label(topFrame, bg = themeColor, font = 24, fg = systemColor, text = usernameText)
usernameLabel.pack()

rankLabel = tkinter.Label(topFrame, bg = themeColor, font = 24, fg = systemColor, text = RankText)
rankLabel.pack()

balanceLabel = tkinter.Label(topFrame, bg = themeColor, font = 24, fg = systemColor, text = BalanceText)
balanceLabel.pack()


EntryField = tkinter.Entry(mainFrame, bg = themeColor, font = 18, fg = userColor, justify = tkinter.CENTER)
EntryField.pack()

RankButton = tkinter.Button(mainFrame, bg = themeColor, font = 24, fg = systemColor, text = 'Set Rank', command = SetRank)
RankButton.pack()

BalanceButton = tkinter.Button(mainFrame, bg = themeColor, font = 24, fg = systemColor, text = 'Set Balance', command = SetBalance)
BalanceButton.pack()


tkinter.mainloop()
