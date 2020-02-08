import urllib.request
import zipfile
import shutil, os, glob
from subprocess import Popen
import sys




def Update():


    url = 'https://github.com/Sasete/LaxtaniaBank/archive/master.zip'


    try:
    
        filelist = glob.glob(os.path.join('./Items', "*.txt"))
        for f in filelist:
            print(str(f) + ', removed')
            os.remove(f)

    try:
        
        os.rmdir('./Items')

    try:

        filelist = glob.glob(os.path.join('./Resources', "*.png"))
        for f in filelist:
            print(str(f) + ', removed')
            os.remove(f)

    try:

        os.rmdir('./Resources')

    try:

        filelist = glob.glob(os.path.join('./', "*.pyw"))
        for f in filelist:
            print(str(f) + ', removed')
            os.remove(f)
        
    try:

        os.remove('./.gitignore')
        
        print('git files removed')

    try:

        os.remove('./Version.txt')


    # Clear Uninstall
    
    
    urllib.request.urlretrieve(url, './LaxtaniaBank.zip')
    

    zipRef = zipfile.ZipFile('./LaxtaniaBank.zip','r')
    zipRef.extractall()    

    print('Zip extracted...')

    zipRef.close()

    shutil.move('./LaxtaniaBank-master/Items','./')

    print('Items are updated...')
    
    shutil.move('./LaxtaniaBank-master/Resources','./')

    print('Resources are updated...')

    shutil.move('./LaxtaniaBank-master/.gitignore', './')

    print('gitignore is updated...')

    
    filelist = glob.glob(os.path.join('./LaxtaniaBank-master/', "*.pyw"))
    for f in filelist:
        shutil.move(f,'./')

    shutil.move('./LaxtaniaBank-master/Version.txt', './')

    print('version updated...')


    os.remove('./Updater2.py')

    
    shutil.move('./LaxtaniaBank-master/Updater2.py', './')

    

    
    print('Apps are updated...')
    
    
    Popen('py Updater2.py')


    sys.exit(0)

    # Gets files back and delete rest



Update()
