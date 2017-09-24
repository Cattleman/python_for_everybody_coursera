"""
@author Hensel
8/25/16

Chapter 7: Files
Resource: https://share.coursera.org/wiki/index.php/Pythonlearn:resources-week07
Working with text files!
Files = secondary memory! 
1) must open a file with open(), return

handle = open(filename,mode) fhand = open('mbox.txt','r')
mode is optional and shout be 'r' to read file or 'w' to write 
filename is a string!

when you open a file it is making a connection between the cpu and RAM
file must be in the same folder as the py code you are running/
to close a file 
fhand.close()

A complete scenario for dealing with a file would thus look like this:

fhand = open("words.txt")
# Do whatever you like with the file contents here, like reading them through a loop.
fhand.close()  # Close the file.

An even more elegant way to write the previous scenario is to use the with statement:
with open("words.txt") as fhand:
    # Do whatever you want here with the file contents.



"""


# "newline" adds puncuation sort of   /n 'x\nY' 'X\nY' is one string! 

#can use a derterminate loop to read a text file

xfile = open('mbox.txt')
for cheese in xfile:
    print cheese
    
# count lines in a file open, use for loop

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print 'Line Count:', count     

#Read the whole file - getting all the lines with /n 
fhand = open('mbox-short.txt')
inp = fhand.read()
print len(inp) #returns the length of the file string

#searching Through a file -- this will search through and find lines with from:
fhand = open('mbox-short.txt')
for line in fhand:
    line =line.rstrip()
    #skip uniteresting \n lines
       if not line.startswith('From:') :
        continue #finishes iteration and starts over
        #process our 'interesting' line 
        print line # print statement adds a \n newline as well as the \n that is on the string so there are two

#promt for a file name
fname= raw_input('Enter the file name: ')
fhand = open(fname) # will have error if file name doesnt exist
count = 0 
for line in fhand:
    if line.startwith('Subject:') : 
        count = count + 1
Print 'There were', count, 'subject lines in', fname

# Using try and except to catch bad file names

fname = raw_input('Enter the file Name: ')
try:
    fhand = open(fname)
except:
    print 'File cannot be found:',fname
    exit()
count = 0 
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print 'There were',count,'subject lines in',fname 
        