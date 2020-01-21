import tkinter
from subprocess import Popen
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import sys
import socket
import time





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


def Info(errTitle, errString):
    messagebox.showinfo(errTitle, errString)


def GetTempData():

    path = './'
    fileName = 'temp.txt'
    
        
    newData = ReadFile(path, fileName)
        
    temp_info = {}

    temp_info["Username"] = newData
    
    
    DeleteFile(path, fileName)

    return temp_info


def BuyCredit():

    
    message = 'BuyCredit/' + userData["Username"] + ',' + dropVar.get()

    amount = int(dropVar.get().split(' ')[0].split('.')[0])
                 
    valueOfCredit = int(105)
    
    print(amount)
    
    AskServer(message)

    Info('Success', 'Your wish successfully sent to server. You have to mail player \'Laxtania\', ' + str(amount * valueOfCredit) + 'g to get your wish accepted.')

    sys.exit(0)




def SellCredit():

    message = 'SellCredit/' + userData["Username"] + ',' + dropVar.get()

    AskServer(message)

    Info('Success', 'Your wish successfully sent to server.')

    sys.exit(0)
    

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

    


userData = GetTempData()

    

main = tkinter.Tk()
main.title('Buy/Sell Credits')
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

dropVar = tkinter.StringVar()
dropVar.set("1.000 Credits")

dropDown = tkinter.OptionMenu(topFrame, dropVar, '1.000 Credits', '2.000 Credits', '3.000 Credits', '4.000 Credits', '5.000 Credits', '6.000 Credits', '7.000 Credits', '8.000 Credits', '9.000 Credits', '10.000 Credits')
dropDown.config(bg = themeColor, activebackground = themeColor, fg = systemColor)
dropDown.pack()

buyButton = tkinter.Button(mainFrame, text = "Buy Credits", bg = themeColor, fg = systemColor, command = BuyCredit)
buyButton.pack(fill = tkinter.X)

sellButton = tkinter.Button(mainFrame, text = "Sell Credits", bg = themeColor, fg = systemColor, command = SellCredit)
sellButton.pack(fill = tkinter.X)





host = "laxtaniabank.ddns.net"
port = 7676


bufferSize = 1024





tkinter.mainloop()
