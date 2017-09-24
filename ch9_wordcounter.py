"""
@author Hensel

Chapter 9: word counting program

"""
name = raw_input('Enterfile:') #ask for file name
handle = open(name,'r') #ask file to open and read
text = handle.read() #read whole file newlines and all, put in variable 'text'
words = text.split() #go through whole string and split to list called 'words'

counts = dict() #creates empty dictionary
for word in words: #for loop that makes each word a key and assigns a value of 1
    counts[word] = counts.get(word,0) + 1 #creates or increments the value of each key

bigcount = None #largest count so far
bigword = None #largest word so far
for word,count in counts.items(): #two value iterative pair
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword,bigcount        