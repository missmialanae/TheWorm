#The Beginning

# Worm 2021 Project By Mia Jenkins and Mentored by Deep Ramanayake

#import modules
import sys #allows for command line and creating files 
import os #allows us access for command line as well but more clear
import glob #helps with replication process and path finding 
import nmap #should allow me to pull from the nmap; may not use
import socket #should allow me to pull the ip address of the host machine of the virus

#######START FUNCTION#########
def start():
    #worm is attached to an email link and when the link is open the worm will execute


################PORTSCAN FUNCTION#############

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

#######END OF PORTSCAN FUNCTION#########

####### COPY FUNCTION#########
def copy(taintfiles):
    #this will make the worm replicate itself in the files

####### HOSTSEARCH FUNCTION #########
def hostsearch:
    #this function is going to allow the worm to search for other host and send the virus 

    #gain access to email app

    #go to the sent email section

    #go through the sent email list and pull the IP and the email addy

    #run portscan on that IP

    #if port scan says open then send the virus

    #if not die

#######SEARCH FUNCTION#########

def search():
    #search through the files and 

    #save pathway

    #place worm in that directory
#######INFECT#########

######PAYLOAD#########

#unload DOS attack 

#set up the DOS attack

#run the attack
portscan()

# The End 