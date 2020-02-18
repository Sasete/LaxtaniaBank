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


# This function reads from file
def ReadFile(m_path, m_fileName):
    filePathName = m_path + m_fileName

    m_file = open(filePathName, 'r')

    m_current = m_file.read()

    m_file.close()

    return m_current


# This function deletes file
def DeleteFile(m_path, m_fileName):
    
    os.remove(m_path + m_fileName)
    

def GetTempData():

    path = './'

    fileName = 'temp.txt'

    
    ReadFile(path, fileName)
    
    DeleteFile(path, fileName)

    return 1


def GetGuildGold():

    gold = AskServer('AdminGold/')

    return gold


def SetGold():

    AskServer('SetGold/' + str(int(EntryField.get())) + ',' + log.get())
    
    UpdatePage()


def AddGold():

    AskServer('AddGold/' + str(int(EntryField.get())) + ',' + log.get())

    UpdatePage()
    


def UpdatePage():

    cashText = 'Guild Gold Depot : ' + GetGuildGold() + 'g'

    cashLabel.config(text = cashText)

    
    

GetTempData()


main = tkinter.Tk()
main.title('Guild Cash')
main.resizable(False,False)


themeColor = "gray"
systemColor = "black"
userColor = "white"


topFrame = tkinter.Frame(main, bg = themeColor, width = 300, height = 100)
topFrame.pack(side = tkinter.TOP, fill = tkinter.X)

divider = tkinter.Frame(main, bg = systemColor, width = 300, height = 2)
divider.pack(side = tkinter.TOP, fill = tkinter.X)

mainFrame = tkinter.Frame(main, bg = themeColor, width = 300, height = 200)
mainFrame.pack(side = tkinter.TOP, fill = tkinter.X)

cashText = 'Guild Gold Depot : ' + GetGuildGold() + 'g'

log = tkinter.StringVar()
log.set('What is here will be added on LOG')

LogField = tkinter.Entry(topFrame, bg = themeColor, font = 18, fg = userColor, justify = tkinter.CENTER, textvariable = log)
LogField.place(width = 300, height = 100)


cashLabel = tkinter.Label(mainFrame, bg = themeColor, font = 24, fg = systemColor, text = cashText)
cashLabel.pack()


cash = tkinter.StringVar()
cash.set('Cash Amount')

EntryField = tkinter.Entry(mainFrame, bg = themeColor, font = 18, fg = userColor, justify = tkinter.CENTER, textvariable = cash)
EntryField.pack()


SetButton = tkinter.Button(mainFrame, bg = themeColor, font = 24, fg = systemColor, text = 'Set Gold', command = SetGold)
SetButton.pack()

AddButton = tkinter.Button(mainFrame, bg = themeColor, font = 24, fg = systemColor, text = 'Add Gold', command = AddGold)
AddButton.pack()


tkinter.mainloop()

