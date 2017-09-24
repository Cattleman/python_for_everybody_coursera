"""
@author: Hensel

8/30/16

Assignment 8.5 : strip out email address

8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

"""

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    print 'File cannot be found.',fname
    exit()

count = 0

for line in fh : 
    if not line.startswith('From ') : continue
    if line.startswith('From ') : 
        from_line = line.strip().split() #strips and splits the line into list  -- we can do both these in one line!
        count = count + 1 
        print from_line[1] #prints the 2nd value in the list which is the email address remember: European elevators! :-)

print "There were", count, "lines in the file with From as the first word"
