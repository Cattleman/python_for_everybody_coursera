"""
@author hensel
8/31/2016

Chapter 9: two iteration varriables!
"""

#We loop through the key-value pairs in a dictionary using *two* iteration variables
#Each iteration the first variable is the key and 
#the second variable is the corresponding VALUE for the key

jjj = {'chuck':1,'fred':32,'jan':100}

for aaa,bbb in jjj.items(): #aaa is the key, bbb is the value and move together in loop
    print aaa,bbb 