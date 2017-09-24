"""
@author: Hensel
9/1/16

Worked Excercise: Chapter 9 - Dictionaries 

"""

name = raw_input('Enter file:') #1st part reads the the whole file
handle = open(name) #open file
text = handle.read() #Read whole file into a string, all newlines will be included become white space in a long list!
words = text.split() #split string into a list

counts = dict() #creates dictionary

for word in words:  #for iterative variable in the list 'words'  
    counts[word] = counts.get(word,0) + 1 #word = key and value is the count 

bigcount = None #define 
bigword = None

for word,count in counts.items() : #two variables, word and count in the dictionary 'counts' 
    if bigcount == None or count > bigcount: #if count is larger than "largest so far" then update bigword and big count to that key value pair
        bigword = word
        bigcount = count 

print bigword, bigcount        