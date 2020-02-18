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

def LOG(m_input):
    info = ReadFile('./', 'Log.txt')


    info += m_input + '/' + str(datetime.now()) + '\n'

    WriteFile('./', 'Log.txt', info)


def GetTempData():

    path = './'
    fileName = 'temp.txt'
    
        
    newData = ReadFile(path, fileName).split(',')
        
    temp_info = {}

    temp_info["ItemName"] = newData[0]
    temp_info["Price"] = newData[1]
    temp_info["Amount"] = newData[2]
    
    
    DeleteFile(path, fileName)

    return temp_info


def SetPrice():

    path = 'Items'

    fileName = itemData["ItemName"]
    
    newPrice = str(EntryField.get())

    newInfo = itemData["ItemName"] + ',' + newPrice + ',' + itemData["Amount"]
    
    AskServer('WriteFile/' + path + ';' + fileName + ';' + newInfo)

    UpdatePage(itemData["ItemName"])
    

def SetAmount():
    
    path = 'Items'

    fileName = itemData["ItemName"]
    
    newAmount = str(EntryField.get())

    newInfo = itemData["ItemName"] + ',' + itemData["Price"] + ',' + newAmount
    
    AskServer('WriteFile/' + path + ';' + fileName + ';' + newInfo)

    UpdatePage(itemData["ItemName"])
    

def GetItemData(itemName):

    iteminfo = AskServer('Details/Items,' + itemName)


    newData =iteminfo.split(',')
        
    temp_info = {}

    temp_info["ItemName"] = newData[0]
    temp_info["Price"] = newData[1]
    temp_info["Amount"] = newData[2]

    return temp_info

    


def UpdatePage(itemName):
    
    item_data = GetItemData(itemName)

    ItemNameText = 'Item Name : ' + item_data["ItemName"]
    PriceText = 'Price : ' + item_data["Price"]  + ' £'
    AmountText = 'Amount : ' + item_data["Amount"]


    itemnameLabel.config(text = ItemNameText)
    priceLabel.config(text = PriceText)
    amountLabel.config(text = AmountText)



itemData = GetTempData()


main = tkinter.Tk()
main.title(itemData["ItemName"])
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

ItemNameText = 'Item Name : ' + itemData["ItemName"]
PriceText = 'Price : ' + itemData["Price"]  + ' £'
AmountText = 'Amount : ' + itemData["Amount"]

itemnameLabel = tkinter.Label(topFrame, bg = themeColor, font = 24, fg = systemColor, text = ItemNameText)
itemnameLabel.pack()

priceLabel = tkinter.Label(topFrame, bg = themeColor, font = 24, fg = systemColor, text = PriceText)
priceLabel.pack()

amountLabel = tkinter.Label(topFrame, bg = themeColor, font = 24, fg = systemColor, text = AmountText)
amountLabel.pack()


EntryField = tkinter.Entry(mainFrame, bg = themeColor, font = 18, fg = userColor)
EntryField.pack()

PriceButton = tkinter.Button(mainFrame, bg = themeColor, font = 24, fg = systemColor, text = 'Set Price', command = SetPrice)
PriceButton.pack()

AmountButton = tkinter.Button(mainFrame, bg = themeColor, font = 24, fg = systemColor, text = 'Set Amount', command = SetAmount)
AmountButton.pack()


tkinter.mainloop()
