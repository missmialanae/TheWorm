# Worm 2021 Project By Mia Jenkins and Mentored by Deep Ramanayake

#import modules
import sys #allows for command line and creating files 
import os #allows us access for command line as well but more clear
import glob #helps with replication process and path finding 
import nmap #should allow me to pull from the nmap; may not use
import socket #should allow me to pull the ip address of the host machine of the virus

#made the portscanner separate since not all victims will use it also offers cleaner code


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
