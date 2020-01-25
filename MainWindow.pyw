import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image
from subprocess import Popen
import os
import sys
import time





def Open(path):
    Popen('py ' + path, shell = True)
    

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

def GetTempDataUser():

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



user_info = GetTempDataUser()


def OpenCredit():

    data = user_info["Username"]

    CreateTempData(data)
    
    Open('./Credit.pyw')

def OpenMarket():
    
    data = user_info["Username"] + ',' + user_info["Balance"]

    CreateTempData(data)
    
    Open('./Market.pyw')
    

def OpenUsers():

    data = user_info["Username"] + ',' + user_info["Balance"]

    
    CreateTempData(data)

    Open('./Users.pyw')
    
    
def CreateTempData(data):
    
    CreateFile('./','temp.txt')
        
    WriteFile('./','temp.txt', data)
    


def CalculateRank(rank):

    # Ranklar, 0 - 1.000 Novice, 1.000 - 10.000 Member, 10.000 - 100.000 Officer, 100.000 - 1M Commander, 1.M < Leader
    if(rank < 1000):
        return 'Novice'
    if(rank < 10000):
        return 'Member'
    if(rank < 100000):
        return 'Officer'
    if(rank < 1000000):
        return 'Commander'
    else:
        return 'Leader'
    


        
main = tkinter.Tk()
main.title("Laxtania")
main.resizable(False,False)

menu = tkinter.Menu(main)
main.config(menu = menu)


guildMenu = tkinter.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Guild", menu = guildMenu)


guildMenu.add_command(label = "Market", command = OpenMarket)
guildMenu.add_command(label = "Send Credits", command = OpenUsers)
guildMenu.add_separator()
guildMenu.add_command(label = "Buy/Sell Credits", command = OpenCredit)


accountMenu = tkinter.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Account", menu = accountMenu)


accountMenu.add_command(label = "Set Profile Picture")
accountMenu.add_separator()
accountMenu.add_command(label = "Change Username")
accountMenu.add_command(label = "Change Password")
accountMenu.add_command(label = "Change E-mail")
accountMenu.add_separator()
accountMenu.add_command(label = "Delete Account")



#themeDark = tkinter.BooleanVar()
#themeDark.set(True)

systemMenu = tkinter.Menu(menu, tearoff = 0)
menu.add_cascade(label = "System", menu = systemMenu)

systemMenu.add_command(label = "Help")
systemMenu.add_command(label = "About")
systemMenu.add_separator()
#systemMenu.add_checkbutton(label = "Dark Mode", onvalue = 1, offvalue = 0, variable = themeDark)
systemMenu.add_command(label = "Exit")


#if(themeDark):
    #themeColor = "gray"
#else:
    #themeColor = "white"

themeColor = "gray"
    

m_height = 400
m_width = 400


sideSpace = 50
topBottomSpace = 125

icon = "./Resources/icon.png"

mainFrame = tkinter.Frame(main, bg = themeColor, height = m_height, width = m_width)
mainFrame.pack(side = tkinter.LEFT, fill = tkinter.Y)


main_image = ImageTk.PhotoImage(Image.open(icon))


mainImage = tkinter.Label(mainFrame, image = main_image, bg = themeColor)
mainImage.pack()


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


username = user_info["Username"]
rank = CalculateRank(int(user_info["Rank"])) + '( ' + user_info["Rank"] + ' points )'
balance = user_info["Balance"] + ' £'


usernameLabel = tkinter.Label(top_sideFrame, bg = themeColor, fg = "black", font = 24, text = username)
usernameLabel.pack()

rankLabel = tkinter.Label(midFrame, bg = themeColor, fg = "black", font = 18, text = rank)
rankLabel.pack()

balanceLabel = tkinter.Label(bot_sideFrame, bg = themeColor, fg = "black", font = 18, text = balance)
balanceLabel.pack()

tkinter.mainloop()
