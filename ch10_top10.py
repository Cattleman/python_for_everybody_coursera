"""
@author Hensel

9/2/16

Chapter 10 - Tuples: Top 10
"""

fhand=open('romeo.txt') #open a file
counts = dict() #empty counts dictionary
for line in fhand: #for loop that reads each line
    words = line.split() #split each line and split to list 
    for word in words: 
        counts[word] = counts.get(word,0) + 1 #look in counts, if word exisits add one or add it to the dict
#at this point we have a dictionary of (word, count) pairs 
lst = list() #create temp list
for key, val in counts.items(): #using the tuples in the counts dictionary
    lst.append( (val, key)) #add to the list (val,key) tuple
lst.sort(reverse=True) #sort the list by the first item in the tuple and sort largest to smallest

for val, key in lst [:10] : #for loop using list slicing 
    print key, val 