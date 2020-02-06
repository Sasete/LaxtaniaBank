import os
import socket
from subprocess import Popen
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter
import sys



host = "laxtaniabank.ddns.net"
port = 7676


bufferSize = 1024




def Open(path):
    Popen('Python ' + path, shell = True)

#This function reads from file
def ReadFile(m_path, m_fileName):
    filePathName = m_path + m_fileName

    m_file = open(filePathName, 'r')

    m_current = m_file.read()

    m_file.close()

    return m_current


# This function deletes file
def DeleteFile(m_path, m_fileName):
    
    os.remove(m_path + m_fileName)

    
def GetTotalCredits():

    totalCredits = AskServer('AdminTotalCredits/')

    return totalCredits

def GetGuildGold():

    gold = AskServer('AdminGold/')

    return gold

def GetMarketSize():

    marketSize = AskServer('AdminMarketSize/')

    return  marketSize


def Error(errTitle, errString):
    messagebox.showerror(errTitle, errString)


def Info(errTitle, errString):
    messagebox.showinfo(errTitle, errString)

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


# This function makes command line wait.
def Wait():

    input("Waiting...")


    return


def OpenUserList():

    CreateTempData('Admin')
    Open('./Userlist.pyw')

def OpenItemList():
    Open('./ItemList.pyw')

def OpenRequestList():
    Open('./RequestList.pyw')

def OpenApplicationList():
    Open('./ApplicationList.pyw')

def OpenWishList():
    Open('./WishList.pyw')
    

# This function checks if 2 given input is matches or not
def doesMatch(str1, str2):

    if(str1 == str2):
        return True
    else:
        return False




def UpdatePage():

    Open('./AdminApp.pyw')
    
    CreateUserData()

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

   
def CreateTempData(data):
    
    CreateFile('./','temp.txt')
        
    WriteFile('./','temp.txt', data)


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

    
def CreateUserData():

    data = user_info["Username"] + ',' +  user_info["Password"] + ',' + user_info["Email"] + ',' + user_info["GM"] + ',' + user_info["Rank"] + ',' + user_info["Balance"]

    CreateTempData(data)


def GoUser():

    CreateUserData()

    Open('./MainWindow.pyw')

    sys.exit(0)

        
main = tkinter.Tk()
main.title("Laxtania")
main.resizable(False,False)

menu = tkinter.Menu(main)
main.config(menu = menu)


guildMenu = tkinter.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Guild", menu = guildMenu)


guildMenu.add_command(label = "Users", command = OpenUserList)
guildMenu.add_command(label = "Items", command = OpenItemList)



manageMenu = tkinter.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Manage", menu = manageMenu)


manageMenu.add_command(label = "Applications", command = OpenApplicationList)
manageMenu.add_command(label = "Wishes", command = OpenWishList)
manageMenu.add_command(label = "Requests", command = OpenRequestList)



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


creditText = 'Total Distributed Laxi : ' + GetTotalCredits() + ' £'
goldText = 'Guild Gold Depot : ' + GetGuildGold() + 'g'
marketText = 'Market size : ' + GetMarketSize() + ' £'


creditLabel = tkinter.Label(midFrame, bg = themeColor, font = 24, text = creditText)
creditLabel.pack()

goldLabel = tkinter.Label(midFrame, bg = themeColor, font = 24, text = goldText)
goldLabel.pack()

marketLabel = tkinter.Label(midFrame, bg = themeColor, font = 24, text = marketText)
marketLabel.pack()

updateButton = tkinter.Button(bot_sideFrame, bg = themeColor, fg = "black", font = 18, text = 'Update', command = UpdatePage)
updateButton.pack()

exitButton = tkinter.Button(bot_sideFrame, bg = themeColor, fg = "black", font = 18, text = 'Return User', command = GoUser)
exitButton.pack()



tkinter.mainloop()







