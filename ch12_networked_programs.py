"""
@author Hensel 

Chapter 12: networked Programs! Uising python to talk to the web!

"""

#peer to peer transport layer 'phone call between applications' 
#SOCKET = connection to applications
#two applications that 'talk' across a network
#apps have a port number - like a phone number extention
#port numbers are connected to various parts of the server, email, web, login etc. 
#ip is the 'phone number' for the server 
"""
Common TCP ports:
telnet(23) - login
SSH(22) - Secoure Login
HTTP(80)
HTTPS(443) - secure
SMTP(25) - mail
IMAP(143/220/993) - Mail retreival
POP (109/110) - Mail Retrieval
DNS (53) - Domain Name
FTP (21) file Transfer
"""

#use python libary 'socket'
#HTTP Hyper text transport protocol  = set of rules that allow brosers to retrieve web docs from servers over internet

#write a web browser
import socket #library
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #method - internet stream socket
mysock.connect( ('www.py4inf.com',80) ) #establish connection and host'www. ' use port 80

mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512) #give you up to 512 characters
    if ( len(data) <1 ) :
        break
    print data
mysock.close()    

#Socket is a low level libary 

#urllib makes it easier!

import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in fhand:
    print line.strip()
    

 