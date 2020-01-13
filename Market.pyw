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

    


    
def SellItem():

    data = 'SellItem/' + userData["Username"] + ',' + str(itemList.get(tkinter.ACTIVE)).split(' ')[2] + ',' + E_amount.get()

    # Get Item Name

    itemName = str(itemList.get(tkinter.ACTIVE)).split(' ')[2]

    print(data)
    AskServer(data)

    Info('Success', 'Your request successfully sent to server. Please send player \'Laxtania\' these materials; ' + E_amount.get() + 'x' + itemName + ' to get your request accepted.')


def BuyItem():
    
    data = 'BuyItem/' + userData["Username"] + ',' + str(itemList.get(tkinter.ACTIVE)).split(' ')[2] + ',' + E_amount.get()

    # Get Cost

    cost = int(itemList.get(tkinter.ACTIVE).split(' ')[6]) * int(E_amount.get())


    AskServer(data)

    Info('Success', 'Your request successfully sent to server. Please send player \'Laxtania\',' + str(cost) + 'g to get your request accepted.')



def UpdateHardware():

    path = './Items/'
    
    items = AskServer('UpdateMarket').split(';')

    files = []

    
    for r,d,f in os.walk(path):
        for file in f:
            if '.txt' in file:
                DeleteFile(path, file)


    for item in items:

        fileName = item.split(',')[0] + '.txt'

        CreateFile(path, fileName)

        WriteFile(path, fileName, item)
        
    


def UpdateItemList():

    UpdateHardware()
    
    path = './Items/'

    files = []

    

    for r,d,f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))


    itemList.delete(0, tkinter.END)
                
    order = 1
    for file in files:

        fileName = str(file).split('.')[1].split('/')[2] + '.txt'

        ItemInfos = ReadFile(path, fileName).split(',')

        itemData = {}

        itemData["ItemName"] = ItemInfos[0]
        itemData["Price"] = ItemInfos[1]
        itemData["Amount"] = ItemInfos[2]

        ListItem = str(order) + ')  ' + itemData["ItemName"]  + '  Price : ' + itemData["Price"] + ' credits  Amount : ' + itemData["Amount"] 
        
        itemList.insert(tkinter.END, ListItem)

        order += 1
        

userData = GetTempData()

        
main = tkinter.Tk()
main.title("Market")
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

itemList = tkinter.Listbox(mainFrame, bg = themeColor, width = 60,font = 20, height = 20, yscrollcommand = scrollbar.set)
itemList.pack()


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


L_username = userData["Username"]
L_balance = userData["Balance"] + ' £'


userNameLabel = tkinter.Label(top_sideFrame, bg = themeColor, fg = systemColor, font = 24, text = L_username)
userNameLabel.pack(side = tkinter.TOP)

balanceLabel = tkinter.Label(top_sideFrame, bg = themeColor, fg = systemColor, font = 18, text = L_balance)
balanceLabel.pack(side = tkinter.BOTTOM)


infoLabel = tkinter.Label(midFrame, bg = themeColor, fg = systemColor, font = 24, text = 'Amount:')
infoLabel.pack(side = tkinter.TOP)

E_amount = tkinter.StringVar()
E_amount.set('0')

EntryField = tkinter.Entry(midFrame, bg = themeColor, fg = userColor, font = 24, textvariable = E_amount, justify = tkinter.CENTER)
EntryField.pack(side = tkinter.TOP)


sellButton = tkinter.Button(midFrame, bg = themeColor, fg = systemColor, text = "Sell", font = 24, width = 10, height = 2, command = SellItem)
sellButton.pack(side = tkinter.BOTTOM)

buyButton = tkinter.Button(midFrame, bg = themeColor, fg = systemColor, text = "Buy", font = 24, width = 10, height = 2, command = BuyItem)
buyButton.pack(side = tkinter.BOTTOM)


exitButton = tkinter.Button(bot_sideFrame, bg = themeColor, fg = systemColor, text = "Exit", font = 24, width = 10, height = 2, command = Close)
exitButton.pack(side = tkinter.BOTTOM)

updateButton = tkinter.Button(bot_sideFrame, bg = themeColor, fg = systemColor, text = "Update", font = 24, width =10, height = 2, command = UpdateItemList)
updateButton.pack(side = tkinter.BOTTOM)




host = "laxtaniabank.ddns.net"
port = 7676


bufferSize = 1024



UpdateItemList()

tkinter.mainloop()
