"""
@author: hensel
8/30/16

Chapter 8 worked Exercise: Lists

Source: https://www.coursera.org/learn/python-data/lecture/t8uFQ/worked-exercise-lists
goal: 
debug a program

"""
#if program chokes on blank lines, use 'Gaurdian pattern!'

fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    words = line.split()
    #print words
    if words == [] : continue #gaurdian pattern - do somthing before the line that breaks. if words is an empty list, continue
    if line == '' : continue # this also works to skip the blank line -- both are not needed, but acomplish same thing
    if words[0] != 'From' : continue
    print words[2] 
    