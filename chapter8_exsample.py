"""
@author: hensel
8/29/16

Chapter 8 list video exsamples
"""

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue #skips lines without 'From'
    words = line.split()
    #print words
    print words[2] #give back third value from each lost (0,1,2 ...) 
    #bellow is double split pattern
    email = word[1]
    pieces = email.split('@')
    host = pieces[1] #gives host of email 
    