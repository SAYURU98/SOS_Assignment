'''
GNS SENARATHNE
IT20647346
SOS(IE2032)-Assignment 2
'''
import os, platform, datetime
from time import gmtime, strftime

#getting the platform name
platformName=platform.platform()


#getting current date and time
dateTimeNow=datetime.datetime.now()

#checking if the os is linux based
if 'Linux' in platformName:
    #creating a path for running user and assigning the path of file to logPathLin variable
    usrHomePath=os.path.expanduser('~')
    logPathLin=usrHomePath+"/Desktop/entries_Lin.log"  #this path won't work on root mode
    fh2=open(logPathLin,'w+')
    #writing os name,date and time with timezone to the file
    fh2.write("Platform Name : "+platformName + '\n'+ '\n')
    fh2.write(dateTimeNow.strftime("%a %B %d %H:%M:%S ")+strftime("%Z", gmtime())+dateTimeNow.strftime(" %Y")+"\n"+"\n")
    fh2.close()
    #searching for bin files in /lib/ and redirecting the output to the entries_Lin.log
    trmCmd='sudo find /lib/ -name "*.bin" -type f >>'+logPathLin
    os.system(trmCmd)
    
#checking if the os is windows
elif 'Windows' in platformName:
    #creating a path for desktop of the running user and assigning the path of file to LogPathWin variable
    wDesktopPath=os.path.join (os.path.expanduser ("~"), "desktop")
    LogPathWin=wDesktopPath+"\entries_Win10.log"
    #writing os name,date and time to the file
    fh=open(LogPathWin,'w+')
    fh.write("Platform Name : "+platformName + '\n')
    fh.write(dateTimeNow.strftime("%d-%b-%Y")+"\n")
    fh.write(dateTimeNow.strftime("%I:%M %p")+'\n')
    fh.close()
    #searching for exe files in sys32 and it's subdirectories and redirecting the output to the entries_Win10.log
    wShellCmd='dir C:\Windows\System32\*.exe /s >>'+LogPathWin  # /s is used to list the exe files in the subdirectories of sys32 folder
    os.system(wShellCmd)
    
    














