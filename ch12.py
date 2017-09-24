import socket #library
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #method - internet stream socket
mysock.connect( ('www.py4inf.com',80) ) #establish connection and host'www. ' use port 80

mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512) #give you up to 512 characters
    if ( len(data) <1 ) :
        break
    print data
mysock.close()    