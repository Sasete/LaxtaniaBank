import urllib.request
import zipfile
import shutil, os, glob



def Update():


    os.remove('./Updater.py')
    shutil.move('./LaxtaniaBank-master/Updater.py', './')


    


    shutil.rmtree('./LaxtaniaBank-master', ignore_errors=True)
    os.remove('./LaxtaniaBank.zip')
    
    
    print('Unnecessary files cleared...')


