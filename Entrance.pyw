import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image
from subprocess import Popen
import subprocess
import sys
import socket
import time



host = "laxtaniabank.ddns.net"
port = 7676


bufferSize = 1024


def Open(path):
    #Popen('Python ' + path, shell = True)
    Popen('py ' + path, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin=subprocess.PIPE  )


# This function reads from file
def ReadFile(m_path, m_fileName):
    filePathName = m_path + m_fileName

    m_file = open(filePathName, 'r')

    m_current = m_file.read()

    m_file.close()

    return m_current   
    

def LogIn():

    m_username = usernameEntry.get()
    m_password = passwordEntry.get()


    server = AskServerForUser(m_username, m_password)
    
    if(server):
    
        Open('./MainWindow.pyw')

        newData = AskUserInfo(m_username)

        CreateTempData(newData)
        
        sys.exit(0)

    else:
        Error("User doesn't Exist", "Wrong Username or Password.")



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




def CreateTempData(data):
    
    CreateFile('./','temp.txt')
        
    WriteFile('./','temp.txt', data)
    

def SignUp():


    Open('./SignUp.pyw')

    
def forgetPass():

    m_username = usernameEntry.get()

    if(m_username == ''):
        Error('Missing Line', 'Please enter a username first...')
    else:

        message = 'ForgetPass/' + m_username
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        
        s.sendto( bytes(message, "utf-8"), (host,port))

        Info('Completed!', 'Please check your e-mail address to learn your password.')

        

def Error(errTitle, errString):
    messagebox.showerror(errTitle, errString)


def Info(errTitle, errString):
    messagebox.showinfo(errTitle, errString)

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

def AskServerForUser(m_username, m_password):


    message = 'LogIn/' + str(m_username) + ',' + str(m_password)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))
        s.send( bytes(message, "utf-8") )


        message = s.recv(bufferSize)
    

        reply = format(message).split('\'')[1]
    
        print(reply)
    
        if(reply == '1'):
            return True
        else:
            return False

    except:
        return Error('Connection Error', 'Server might not be listening currently...')
        
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
    

def CheckVersion():

    try:

        version = ReadFile('./', 'Version.txt')

        serverVersion = AskServer('Version/')


        if(version < serverVersion):

            Open('./Updater.py')

            sys.exit(0)

            return

        return

    except:

        Open('./Updater.py')

        sys.exit(0)

        return
        


CheckVersion()

        
main = tkinter.Tk()
main.title("Laxtania")
main.resizable(False,False)


colorTheme = "gray"
systemTheme = "black"
userTheme = "white"


m_height = 400
m_width = 400


sideSpace = 50
topBottomSpace = 125

icon = "./Resources/icon.png"

mainFrame = tkinter.Frame(main, bg = colorTheme, height = m_height, width = m_width)
mainFrame.pack(side = tkinter.LEFT, fill = tkinter.Y)


main_image = ImageTk.PhotoImage(Image.open(icon))


mainImage = tkinter.Label(mainFrame, image = main_image, bg = colorTheme)
mainImage.pack()


s_height= 400
s_width = 200

sideFrame = tkinter.Frame(main, bg = colorTheme, height = s_height, width = s_width)
sideFrame.pack(side = tkinter.RIGHT , fill = tkinter.Y)

divider = tkinter.Frame(main, bg = "black", height = s_height, width = 2)
divider.pack(side = tkinter.RIGHT, fill = tkinter.Y)



left_sideFrame = tkinter.Frame(sideFrame, bg = colorTheme, height = s_height, width = sideSpace)
left_sideFrame.pack(side = tkinter.LEFT, fill = tkinter.Y)



right_sideFrame = tkinter.Frame(sideFrame, bg = colorTheme, height = s_height, width = sideSpace)
right_sideFrame.pack(side = tkinter.RIGHT, fill = tkinter.Y)

mid_sideFrame = tkinter.Frame(sideFrame, bg = colorTheme, height = s_height, width = s_width - 2 * sideSpace)
mid_sideFrame.pack(side = tkinter.RIGHT, fill = tkinter.Y)




top_sideFrame = tkinter.Frame(mid_sideFrame, bg = colorTheme, height = topBottomSpace)
top_sideFrame.pack(side = tkinter.TOP, fill = tkinter.X)


#top_icon = './Resources/top_icon.png'

#top_image = ImageTk.PhotoImage(Image.open(top_icon))

#topImage = tkinter.Label(top_sideFrame, image = top_image, bg = "gray")
#topImage.pack(side = "bottom")


bot_sideFrame = tkinter.Frame(mid_sideFrame, bg = colorTheme, height = topBottomSpace)
bot_sideFrame.pack(side = tkinter.BOTTOM, fill = tkinter.X)

midFrame = tkinter.Frame(mid_sideFrame, bg = colorTheme, height = topBottomSpace)
midFrame.pack(side = tkinter.TOP, fill = tkinter.X)


username = tkinter.StringVar()
username.set("")

entryWidth = 20

u_text = "Username :"

usernameText = tkinter.Label(midFrame, bg = colorTheme, fg = systemTheme, text = u_text)
usernameText.pack()

usernameEntry = tkinter.Entry(midFrame, bg = colorTheme, fg = userTheme, width = entryWidth, textvariable = username, justify = tkinter.CENTER)
usernameEntry.pack()

p_text = "Password :"

passwordText = tkinter.Label(midFrame, bg = colorTheme, fg = systemTheme, text = p_text)
passwordText.pack()

password = tkinter.StringVar()
password.set("")

passwordEntry = tkinter.Entry(midFrame, show = "*", bg = colorTheme, fg = userTheme, width = entryWidth, textvariable = password, justify = tkinter.CENTER)
passwordEntry.pack()


loginButton = tkinter.Button(midFrame, bg = colorTheme, fg = systemTheme, text = "Log in", width = 12, font = 1, command = LogIn)
loginButton.pack()


def loginTkinter(event):
    LogIn()

main.bind('<Return>', loginTkinter)




signUpButton = tkinter.Button(midFrame, bg = colorTheme, fg = systemTheme, text = "Sign up", width = 12, font = 1, command = SignUp)
signUpButton.pack()


forgetPassButton = tkinter.Button(midFrame, bg = colorTheme, fg = systemTheme, text = "Forget Password", width = 12, command = forgetPass)
forgetPassButton.pack()







tkinter.mainloop()
