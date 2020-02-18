import tkinter
from subprocess import Popen
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import sys
from datetime import datetime
import socket
import signal




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
    
    #os.remove(m_path + m_fileName)

    return


def Change():


    newInfo = EntryField.get()

    AskServer('Change' + ChangeType + '/' + oldInfo + ',' + newInfo)


    Info('Success', 'Your change operation successfully done. Your application will close itself. Please LogIn again with new information...')

    os.kill(pid, signal.SIGTERM)


    sys.exit(0)

    return


def GetTempData():

    path = './'

    fileName = 'temp.txt'

    
    fileInfo = ReadFile(path, fileName)
    
    DeleteFile(path, fileName)

    return fileInfo


ChangeType = GetTempData().split(',')[0]
oldInfo = GetTempData().split(',')[1]
pid = int(GetTempData().split(',')[2])


main = tkinter.Tk()
main.title('Change ' + ChangeType)
main.resizable(False,False)


themeColor = "gray"
systemColor = "black"
userColor = "white"


mainFrame = tkinter.Frame(main, bg = themeColor, width = 300, height = 200)
mainFrame.pack(side = tkinter.TOP, fill = tkinter.X)


entryText = tkinter.StringVar()
entryText.set(ChangeType)

setText = tkinter.StringVar()
setText.set('Change ' + ChangeType)

EntryField = tkinter.Entry(mainFrame, bg = themeColor, font = 18, fg = userColor, justify = tkinter.CENTER, textvariable = entryText)
EntryField.pack()



ChangeButton = tkinter.Button(mainFrame, bg = themeColor, font = 24, fg = systemColor, text = setText.get(), command = Change)
ChangeButton.pack()




tkinter.mainloop()





