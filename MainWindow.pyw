import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image
from subprocess import Popen
import os
import sys
import socket
import time
import webbrowser
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





def OpenURL(url):
    webbrowser.open(url, new=2)

def OpenItemBuilder():
    OpenURL('https://archeagecalculator.com/#')

def OpenCargoShipTracker():
    OpenURL('http://aau-cargo.com/Halnaak/actual')

    

def OpenDailiesMokulu():
    OpenURL('https://archeage.mokulu.io/dailies')

def OpenSkillsMokulu():
    OpenURL('https://archeage.mokulu.io/skills')
    
def OpenCommerceMokulu():
    OpenURL('https://archeage.mokulu.io/trade-packs')

def OpenScheduleMokulu():
    OpenURL('https://archeage.mokulu.io/schedule')

def OpenMountsMokulu():
    OpenURL('https://archeage.mokulu.io/mounts')

def OpenTaxesMokulu():
    OpenURL('https://archeage.mokulu.io/taxes')

def OpenThunderMokulu():
    OpenURL('https://archeage.mokulu.io/thunderstruck')

    




def Open(path):
    Popen('py ' + path, shell = True)
    

def Exit():

    Open('./Entrance.pyw')
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



def AskUserInfo(m_username):

    message = 'UserInfo/' + str(m_username)
    
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


def UpdatePage():


    username = user_info["Username"]
    rank = CalculateRank(int(user_info["Rank"])) + '( ' + user_info["Rank"] + ' points )'
    balance = GetUserGold(user_info["Username"]) + ' £'
    rValue = '£ Real Value: ' + str(float("{:.2f}".format(float(AskRValue())))) + 'g'
    iValue = '£ Image Value: ' + str(float("{:.2f}".format(float(AskValue())))) + 'g'


    usernameLabel.config(text = username)
    rankLabel.config(text = rank)
    balanceLabel.config(text = balance)
    valueLabel.config(text = iValue)
    rvalueLabel.config(text = rValue)
    

def GetUserGold(m_username):

    userInfo = AskUserInfo(str(m_username))

    newData = userInfo.split(',')

    temp_info = {}

    temp_info["Username"] = newData[0]
    temp_info["Password"] = newData[1]
    temp_info["Email"] = newData[2]
    temp_info["GM"] = newData[3]
    temp_info["Rank"] = newData[4]
    temp_info["Balance"] = newData[5]

    return temp_info["Balance"]


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

def CreateUserData():

    data = user_info["Username"] + ',' +  user_info["Password"] + ',' + user_info["Email"] + ',' + user_info["GM"] + ',' + user_info["Rank"] + ',' + user_info["Balance"]

    CreateTempData(data)



def OpenAdminApp():
    if(int(user_info["Rank"]) >= 100000):
        Open('./AdminApp.pyw')
        CreateUserData()
        sys.exit(0)
    else:
        return Error('Access Denied', 'Access denied. Not enough Authority...')

    
    
def CreateTempData(data):
    
    CreateFile('./','temp.txt')
        
    WriteFile('./','temp.txt', data)
    

def AskRValue():

    value = AskServer('RealValue/')


    return value



def AskValue():

    value = AskServer('ImageValue/')

    return value


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
    

def ChangeUsername():


    CreateTempData('Username,' + user_info["Username"] + ',' + str(os.getpid()))

    Open('./Change.pyw')

    return


def ChangePassword():


    CreateTempData('Password,' + user_info["Password"] + ',' + str(os.getpid()))

    Open('./Change.pyw')
    

    return


def ChangeEmail():

    CreateTempData('Email,' + user_info["Email"] + ',' + str(os.getpid()))

    Open('./Change.pyw')
    

    return


        
main = tkinter.Tk()
main.title("Laxtania")
main.resizable(False,False)

menu = tkinter.Menu(main)
main.config(menu = menu)


guildMenu = tkinter.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Guild", menu = guildMenu)



guildMenu.add_command(label = "Market", command = OpenMarket)
guildMenu.add_command(label = "Send Laxi\'s", command = OpenUsers)
guildMenu.add_separator()
guildMenu.add_command(label = "Buy/Sell Laxi", command = OpenCredit)


toolsMenu = tkinter.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Tools", menu = toolsMenu)

mokuluMenu = tkinter.Menu(toolsMenu, tearoff = 0)
mokuluMenu.add_command(label = "Dailies", command = OpenDailiesMokulu)
mokuluMenu.add_command(label = "Skills", command = OpenSkillsMokulu)
mokuluMenu.add_command(label = "Trade Packs", command = OpenCommerceMokulu)
mokuluMenu.add_command(label = "Schedule", command = OpenScheduleMokulu)
mokuluMenu.add_command(label = "Mounts", command = OpenMountsMokulu)
mokuluMenu.add_command(label = "Taxes", command = OpenTaxesMokulu)
mokuluMenu.add_command(label = "Thunderstruck", command = OpenThunderMokulu)


toolsMenu.add_command(label = "Cargo Ship Tracker", command = OpenCargoShipTracker)
toolsMenu.add_command(label = "Treasure Hunt Helper")
toolsMenu.add_command(label = "Gear Builder", command = OpenItemBuilder)
toolsMenu.add_separator()
toolsMenu.add_cascade(label = "Mokulu Tools", menu = mokuluMenu)


accountMenu = tkinter.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Account", menu = accountMenu)



accountMenu.add_command(label = "Administrative", command = OpenAdminApp)
accountMenu.add_separator()
accountMenu.add_command(label = "Change Username", command = ChangeUsername)
accountMenu.add_command(label = "Change Password", command = ChangePassword)
accountMenu.add_command(label = "Change E-mail", command = ChangeEmail)
accountMenu.add_separator()
accountMenu.add_command(label = "Log Out", command = Exit)



#themeDark = tkinter.BooleanVar()
#themeDark.set(True)




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
balance = GetUserGold(user_info["Username"]) + ' £'
rValue = '£ Real Value: ' + str(float("{:.2f}".format(float(AskRValue())))) + 'g'
iValue = '£ Image Value: ' + str(float("{:.2f}".format(float(AskValue())))) + 'g'


usernameLabel = tkinter.Label(top_sideFrame, bg = themeColor, fg = "black", font = 24, text = username)
usernameLabel.pack()

rankLabel = tkinter.Label(midFrame, bg = themeColor, fg = "black", font = 18, text = rank)
rankLabel.pack()

rvalueLabel = tkinter.Label(bot_sideFrame, bg = themeColor, fg = "black", font = 18, text = rValue)
rvalueLabel.pack()

valueLabel = tkinter.Label(bot_sideFrame, bg = themeColor, fg = "black", font = 18, text = iValue)
valueLabel.pack()

balanceLabel = tkinter.Label(bot_sideFrame, bg = themeColor, fg = "black", font = 18, text = balance)
balanceLabel.pack()

updateButton = tkinter.Button(bot_sideFrame, bg = themeColor, fg = "black", font = 18, text = 'Update', command = UpdatePage)
updateButton.pack()

def updatetkinter(event):
    UpdatePage()

main.bind('r', updatetkinter)



host = "laxtaniabank.ddns.net"
port = 7676


bufferSize = 1024



tkinter.mainloop()
