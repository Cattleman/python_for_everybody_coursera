# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 12:09:56 2016
@author: Hensel

String Comparisions - Chapter 6 video 'Strings'
~~~~~~~
RESOURCE: https://docs.python.org/2/library/stdtypes.html#string-methods
#can do comparisons of equality ==  less and greater than > <
Extensive string library
"""

greet = 'Hello Bob'
zap = greet.lower()  #give back greet in lower case. 
print zap 

dir(greet) #used in comand prompt >>> dir() will tell you all  the features of the string you can manipulate

nstr = greet.replace('Bob','Jane')

#Stripping whitespace

greet = ' Hello Bob ' #extra spaces on both sides of string
greet.lstrip() #strips from left
greet.rstrip() #strips from right
greet.strip() #both sides


#when looking at data we may want a prefix

line = 'please have a nice day'
line.startswith('Please')
#returns true

line.startswith('p')
# returns False

