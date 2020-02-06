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


def GetTempData():

    path = './'

    fileName = 'temp.txt'

    
    ReadFile(path, fileName)
    
    DeleteFile(path, fileName)

    return 1

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


# This function creates empty file
def CreateFile(m_path, m_fileName):
    WriteFile(m_path, m_fileName, '')

    return


# This function deletes file
def DeleteFile(m_path, m_fileName):
    
    os.remove(m_path + m_fileName)


def LOG(m_input):
    info = ReadFile('./', 'Log.txt')


    info += m_input + '/' + str(datetime.now()) + '\n'

    WriteFile('./', 'Log.txt', info)


def Error(errTitle, errString):
    messagebox.showerror(errTitle, errString)


def AddItem():

    

    itemName = str(E_itemname.get())
    amount = str(E_amount.get())
    price = str(E_price.get())

    newData = itemName + ';' + price + ';' + amount

    AskServer('AddItem/' + newData)


        
GetTempData()

main = tkinter.Tk()
main.title('Add Item')
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

itemname = tkinter.StringVar()
itemname.set('Item Name')

price = tkinter.StringVar()
price.set('Price')

amount = tkinter.StringVar()
amount.set('Amount')

E_itemname = tkinter.Entry(topFrame, bg = themeColor, font = 18, fg = userColor, justify = tkinter.CENTER, textvariable = itemname)
E_itemname.pack()

E_price = tkinter.Entry(topFrame, bg = themeColor, font = 18, fg = userColor, justify = tkinter.CENTER, textvariable = price)
E_price.pack()

E_amount = tkinter.Entry(topFrame, bg = themeColor, font = 18, fg = userColor, justify = tkinter.CENTER, textvariable = amount)
E_amount.pack()


AddButton = tkinter.Button(mainFrame, bg = themeColor, font = 24, fg = systemColor, text = 'Add Item', command = AddItem)
AddButton.pack()


tkinter.mainloop()
