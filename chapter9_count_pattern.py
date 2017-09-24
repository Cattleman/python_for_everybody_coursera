"""
@hensel

Chapter 9: Counting Pattern
"""

counts = dict() #crates a dictionary
print 'Enter a line of text:'
line = raw_input('') #prompts for input

words = line.split() #splits string into list, list maintains the order of the input 
print 'Words:',words

print 'Counting...'
for word in words: # 'word' is the iterative variable of the list'words'
    counts[word] = counts.get(word,0) + 1 # this will either create or update dictionary 
print 'Counts',counts 