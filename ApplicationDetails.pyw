import tkinter
from subprocess import Popen
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import sys




# This function reads from file
def ReadFile(m_path, m_fileName):
    filePathName = m_path + m_fileName

    m_file = open(filePathName, 'r')

    m_current = m_file.read()

    m_file.close()

    return m_current

# This function deletes file
def DeleteFile(m_path, m_fileName):
    
    os.remove(m_path + m_fileName)
    
def GetTempData():

    path = './'
    fileName = 'temp.txt'
    
        
    newData = ReadFile(path, fileName).split(',')
        
    temp_info = {}

    temp_info["Username"] = newData[0]
    temp_info["Password"] = newData[1]
    temp_info["Email"] = newData[2]
    
    
    DeleteFile(path, fileName)

    return temp_info



applicationData = GetTempData()


main = tkinter.Tk()
main.title('Application')
main.resizable(False,False)


themeColor = "gray"
systemColor = "black"
userColor = "white"


topFrame = tkinter.Frame(main, bg = themeColor, width = 300, height = 200)
topFrame.pack(side = tkinter.TOP, fill = tkinter.X)


usernameText = 'Username : ' + applicationData["Username"]
mailText = 'Email : ' + applicationData["Email"]


usernameLabel = tkinter.Label(topFrame, bg = themeColor, font = 24, fg = systemColor, text = usernameText)
usernameLabel.pack()

mailLabel = tkinter.Label(topFrame, bg = themeColor, font = 24, fg = systemColor, text = mailText)
mailLabel.pack()




tkinter.mainloop()

