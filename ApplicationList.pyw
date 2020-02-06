import tkinter
from subprocess import Popen
from tkinter import messagebox
from PIL import ImageTk, Image
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import sys
from datetime import datetime


def Open(path):
    Popen('Python ' + path, shell = True)

def Close():
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

# This function deletes file
def DeleteFile(m_path, m_fileName):
    
    os.remove(m_path + m_fileName)


def CreateTempData(data):
    
    CreateFile('./','temp.txt')
        
    WriteFile('./','temp.txt', data)
    
# This function writes into file with deleting previously info
def WriteFile(m_path, m_fileName, m_data):

    m_file = open(m_path + m_fileName, 'w')

    m_file.write(m_data)

    m_file.close()

    return

def Details():

    path = './Applications/'

    fileName = str(applicationList.get(tkinter.ACTIVE).split(' ')[2]) + '.txt'

    newInfo = ReadFile(path, fileName)

    CreateTempData(newInfo)

    Open('./ApplicationDetails.pyw')

def LOG(m_input):
    info = ReadFile('./', 'Log.txt')


    info += m_input + '/' + str(datetime.now()) + '\n'

    WriteFile('./', 'Log.txt', info)


def Confirm():

    path = './Applications/'
    fileName = str(applicationList.get(tkinter.ACTIVE).split(' ')[2]) + '.txt'

    newInfo = ReadFile(path, fileName).split(',')
    
    applicationData = {}

    applicationData["Username"] = newInfo[0]
    applicationData["Password"] = newInfo[1]
    applicationData["Email"] = newInfo[2]
      
    path = './Users/'
    
    CreateFile(path, fileName)

    newData = applicationData["Username"] + ',' +applicationData["Password"] + ',' + applicationData["Email"] + ',' + '0' + ',' + '0' + ',' + '0'

    WriteFile(path, fileName, newData)

    msg = MIMEMultipart()
    
    msg["From"] = "laxialaxtania@gmail.com"

    msg["To"] = applicationData["Email"]
        
    msg["Subject"] = "Sign Up Request"


    body = "Your signation has completed! Thank you for joining us!"
    #server.sendmail("laxialaxtania@gmail.com",GetUserMail(m_username),msg)

    logInfo = 'New user added: ' + newData

    LOG(logInfo)

    SendMail(msg, str(body))

    path = './Applications/'
    DeleteFile(path, fileName)

    UpdateApplicationList()
        
def SendMail(message, body):

    
    body_text = MIMEText(body,"plain") #

    message.attach(body_text)

    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)  

        mail.ehlo()

        mail.starttls()    

        mail.login("laxialaxtania@gmail.com","!Qwerty12345")

        mail.sendmail(message["From"],message["To"],message.as_string())

        print("Mail Başarılı bir şekilde gönderildi.")

        mail.close()
    #Eğer mesaj gönderirken hata ile karşılaşırsak except çalışır.
    except:
        sys.stderr.write("Bir hata oluştu. Tekrar deneyin...\n")
        sys.stderr.flush()
    

    

def Reject():
    
    path = './Applications/'

    fileName = str(applicationList.get(tkinter.ACTIVE).split(' ')[2]) + '.txt'

    DeleteFile(path, fileName)

    UpdateApplicationList()

    logInfo = 'Application rejected!' + fileName

    LOG(logInfo)

def UpdateApplicationList():
    
    path = './Applications/'

    files = []

    

    for r,d,f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))


    applicationList.delete(0, tkinter.END)
                
    order = 1
    for file in files:

        fileName = str(file).split('.')[1].split('/')[2] + '.txt'

        applicationInfos = ReadFile(path, fileName).split(',')

        applicationData = {}

        applicationData["Username"] = applicationInfos[0]
        applicationData["Password"] = applicationInfos[1]
        applicationData["Email"] = applicationInfos[2]

        ListItem = str(order) + ')  ' + applicationData["Username"]
        
        applicationList.insert(tkinter.END, ListItem)

        order += 1
        


       
main = tkinter.Tk()
main.title("Application List")
main.resizable(False,False)

themeColor = "gray"
systemColor = "black"
    

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

applicationList = tkinter.Listbox(mainFrame, bg = themeColor, width = 60,font = 20, height = 20, yscrollcommand = scrollbar.set)
applicationList.pack()


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


RejectButton = tkinter.Button(midFrame, bg = themeColor, fg = systemColor, text = "Reject", font = 24, width = 10, height = 2, command = Reject)
RejectButton.pack(side = tkinter.BOTTOM)

ConfirmButton = tkinter.Button(midFrame, bg = themeColor, fg = systemColor, text = "Confirm", font = 24, width = 10, height = 2, command = Confirm)
ConfirmButton.pack(side = tkinter.BOTTOM)

DetailsButton = tkinter.Button(midFrame, bg = themeColor, fg = systemColor, text = "Details", font = 24, width = 10, height = 2, command = Details)
DetailsButton.pack(side = tkinter.BOTTOM)

exitButton = tkinter.Button(bot_sideFrame, bg = themeColor, fg = systemColor, text = "Exit", font = 24, width = 10, height = 2, command = Close)
exitButton.pack(side = tkinter.BOTTOM)

updateButton = tkinter.Button(bot_sideFrame, bg = themeColor, fg = systemColor, text = "Update", font = 24, width =10, height = 2, command = UpdateApplicationList)
updateButton.pack(side = tkinter.BOTTOM)




UpdateApplicationList()

tkinter.mainloop()

