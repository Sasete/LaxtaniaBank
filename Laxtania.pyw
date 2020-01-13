from subprocess import Popen
import subprocess
import sys



def Open(path):
    Popen('py ' + path, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin=subprocess.PIPE  )
    
    


Open('./Entrance.pyw')

sys.exit()
