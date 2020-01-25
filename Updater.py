import urllib.request
import zipfile
import shutil, os, glob





def Update():


    url = 'https://github.com/Sasete/LaxtaniaBank/archive/master.zip'


    
    
    filelist = glob.glob(os.path.join('./Items', "*.txt"))
    for f in filelist:
        print(str(f) + ', removed')
        os.remove(f)

    os.rmdir('./Items')


    filelist = glob.glob(os.path.join('./Resources', "*.png"))
    for f in filelist:
        print(str(f) + ', removed')
        os.remove(f)

    os.rmdir('./Resources')

    filelist = glob.glob(os.path.join('./', "*.pyw"))
    for f in filelist:
        print(str(f) + ', removed')
        os.remove(f)
        

    os.remove('./.gitignore')

    print('git files removed')

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

    
    print('Apps are updated...')
    

    shutil.rmtree('./LaxtaniaBank-master', ignore_errors=True)
    os.remove('./LaxtaniaBank.zip')
    
    
    print('Unnecessary files cleared...')

    # Gets files back and delete rest



Update()
