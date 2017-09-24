"""
@author Hensel

Chapter 11: Regular Expressions

In computing, a regular expression, also referred to as a "regex" or "regexp", provides a concise and fleible means for matching strings of text,
such as particular characters, words or patterns of characters. A regular expression is written in a formal language that can be 
interpereted by a regular expression processor. 
"""

#reg exp are their own tiny programing language used in lots of programing languages for 
#cross string matching. 
#regexp uses characters - characters have meaning
#MUST import regexp with 'import re'


"""
#SEARCH
re.search() #see if a string matches a reg exp, similar to find() for strings - returns a T/F
re.findall() - combo of find() and slicing
"""

#Using re.search() like find()

"""
hand = open('mbox-short.txt')
for line in hand:
    line =line.rstrip()
    if line.find('From: ') >= 0:
        print line 
#equivilant code:
"""
import re #imprt the re library 
hand = open('mbox-short.txt') #open file 
for line in hand: #loop through file
    line = line.rstrip() #strip
    if re.search('X-\S+:', line) : #look though line, find 'from:' uses ^ to look at from at beg of line
        print line 
#re.search() returns a True/False depending on whether the string matches the regular expression
#if we actually want the matching strings to be extracted, we use re.findall()

#re.findall() returns a list
 
import re
x = 'From: Using the : character' 
y = re.findall('^F.+?:', x) 
print y #returns ['From:']

#FINE-TUNING STRING EXTRACTION
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x) #uses greedy behavior to extend from '@' in both directions      
print y  

#can use '(parentheses )' to fine tune and make a longer expression
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)', x)    #includes the space in the ''  
print y  

#another regex way to do this - take out domain host 
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008' 
y = re.findall('^From .*@([^ ]*)',lin) #[^ ]* means many non blank characters
print y 