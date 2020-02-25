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

    except:
        print('Couldn\'t find items.')
        

    try:
        
        os.rmdir('./Items')

    except:
        print('Couldn\'t find items folder.')

    

    try:

        filelist = glob.glob(os.path.join('./Resources', "*.png"))
        for f in filelist:
            print(str(f) + ', removed')
            os.remove(f)

    except:
        print('Couldn\'t find resources.')
    

    try:

        os.rmdir('./Resources')

    except:
        print('Couldn\'t find resources file.')

    try:

        filelist = glob.glob(os.path.join('./', "*.pyw"))
        for f in filelist:
            print(str(f) + ', removed')
            os.remove(f)


    except:
        print('Couldn\'t find any .pyw file.')
        
    try:

        os.remove('./.gitignore')
        
        print('git files removed')

    except:
        print('Couldn\'t find git files.')

    try:

        os.remove('./Version.txt')

    except:
        print('Couldn\'t find version file.')


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


    try:

        shutil.move('./LaxtaniaBank-master/Laxtania.exe.lnk', './')

    except:

        print('Shortcut is exist.')

        

    
    print('Apps are updated...')
    
    
    Popen('py Updater2.py')


    sys.exit(0)

    # Gets files back and delete rest



Update()
