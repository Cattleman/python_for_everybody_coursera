# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:30:31 2016

@author: Hensel

Strings: Chapter 6 


"""
#we can get at ant string character in a tring using an index specified in square brakets[] 
# 0 is the 1st value of the string

fruit = 'banana'
letter = fruit[1] # 1 vaule is 2nd value in the string above or a
print letter

# len() can be used to tell how many characters are in a string or length of a string
x = len(fruit)
print x

#string loops - indefinite 

#uses fruit deffinition above

index = 0 
while index < len(fruit):
    letter = fruit[index]
    print index, letter
    index = index + 1
    
# DEFINTE loop the iteration variable is taken care of by the for loop

fruit = 'banana'
for letter in fruit: # for each value in fruit, print each value  for and in comand sets up the index 
    print letter     

# looping and counting
word = 'bannana' 
count = 0 
for letter in word:
    if letter =='a':

"""
#Slicing Strings can use colon operatior : to look at a contunous section of a strung
exsample:

s = 'Monty python'
print s[0:4]

^the 4 is one value beyond "up to but not including"
if the second number is beyond the end of the sring it stops at the end

"""        
s = 'Monty python'
print s[0:4]
print s[6:7]
print s[6:20] #will stop at end of string!

"""
String Concatenation

the + opperator doenst add a space. must be added as ' ' 
"""

a = 'hello'
b = a + 'There'
print b

c = a + ' ' +'There'
print c

"""
Using the 'in' opperator
can be used to check to see if a string is in another string
the in expression is a logical expression and returns True or False statement can be used in an 'if' statement

"""
fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit

if 'a' in fruit :
        print 'Found it!' 
        
