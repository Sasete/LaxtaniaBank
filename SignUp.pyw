import tkinter
from tkinter import messagebox
import socket
import sys



host = "176.233.32.178"
port = 7676


def SignUp():

    m_email = email.get()
    m_username = username.get()
    m_password = password.get()

    message = 'SignUp/' + m_email + ',' + m_username + ',' + m_password


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host,port))
    
    s.send( bytes(message, "utf-8") )

    Reply('Completed!','Your application has been sent to server, once you\'ve accepted, you\'ll get an email about it. Thanks for joining...')

    
    sys.exit(0)


def Reply(errTitle, errString):
    messagebox.showinfo(errTitle, errString)
    

main = tkinter.Tk()
main.title("Sign Up")
main.resizable(False,False)


colorTheme = "gray"
systemTheme = "black"
userTheme = "white"


windowFrame = tkinter.Frame(main, bg = colorTheme, width = 240, height = 20)
windowFrame.pack(side = tkinter.TOP, fill = tkinter.X)


windowFrame2 = tkinter.Frame(main, bg = colorTheme, width = 240, height = 20)
windowFrame2.pack(side = tkinter.BOTTOM, fill = tkinter.X)


mainFrame = tkinter.Frame(main, bg = colorTheme, width = 240, height = 540)
mainFrame.pack(side = tkinter.BOTTOM, fill = tkinter.X)

e_text = "E-Mail :"

email = tkinter.StringVar()
email.set("")

emailText = tkinter.Label(mainFrame, bg = colorTheme, fg = systemTheme, text = e_text)
emailText.pack()


emailEntry = tkinter.Entry(mainFrame, bg = colorTheme, fg = userTheme, textvariable = email, justify = tkinter.CENTER)
emailEntry.pack()



username = tkinter.StringVar()
username.set("")

u_text = "Username :"

usernameText = tkinter.Label(mainFrame, bg = colorTheme, fg = systemTheme, text = u_text)
usernameText.pack()

usernameEntry = tkinter.Entry(mainFrame, bg = colorTheme, fg = userTheme, textvariable = username, justify = tkinter.CENTER)
usernameEntry.pack()

p_text = "Password :"

passwordText = tkinter.Label(mainFrame, bg = colorTheme, fg = systemTheme, text = p_text)
passwordText.pack()

password = tkinter.StringVar()
password.set("")

passwordEntry = tkinter.Entry(mainFrame, show = "*", bg = colorTheme, fg = userTheme, textvariable = password, justify = tkinter.CENTER)
passwordEntry.pack()



signUpButton = tkinter.Button(mainFrame, bg = colorTheme, fg = systemTheme, text = "Sign up", width = 8, command = SignUp)
signUpButton.pack()




tkinter.mainloop()

