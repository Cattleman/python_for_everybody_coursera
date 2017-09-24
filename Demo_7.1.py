"""
@author: Hensel
8/29/16

Demonstration problem from excersie 7.1  <<-- not 7.6 book was updated
source: https://www.coursera.org/learn/python-data/lecture/197Re/demonstration-worked-exercise-7-6

This program will access the file and capitalize all the letters

"""

fname = raw_input('what file would you like to capitalize?')
#bellow creates a default
if len(fname) == 0:
    fname = 'mbox-short.txt'
try:
    fhand = open(fname)

except:
    print 'Unable to find file'
    exit()

    
    #remember that 'line' is a variable name  
for line in fhand : 
    line = line.strip().upper() # must trim extra \n AND capitalze 
    line = line.
    print line 