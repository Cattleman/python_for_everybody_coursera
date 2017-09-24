"""
Week 6 chapter 4
Functions!

arguments go inside the () of the function as inputs.
arguments direct the fuction to do different kinds of work when we call it at dufferent times.

"""

def hello():
    print 'hello'
    print 'fun'
    
hello()


#lang is a place holder variable/argument
def greet(lang):
    if lang =='es':
        return 'Hola'
    elif lang == 'fr':
        print 'Bonjoiur'
    else:
        print 'Hello'


greet('en')
greet('es')
greet('fr')

def greet1():
    return 'hello'
    
print greet1(),"glenn"    

def addtwo(a,b):
    added = a + b
    return added
    
x = addtwo(3,5)
print x     

# when a function does not return a value, we call it a "void" function
#functions that return values are "fruitful" functions
# void functions are "not fruitful"


