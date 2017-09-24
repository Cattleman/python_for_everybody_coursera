""""
@author Hensel
8/29/2016

Chapter 8: Lists

#list has  [square braces]
#a list is a kind of collection and allows us to put more than one thing in a varriable 
#simple varriables are not collections, we've been using list constants ie. [1,24,76] or ['red','yellow']
# can have mix of strings and float or ints 
# lists can also nest[1,[3,4],5]
# 1st item in a list is 0! remember euro elevator!
#lists are mutable <-- can be changed
#strings are NOT mutable
#len() can be used to find number of items in a list just like a strings

What can we do with a list if type = list append, count, extend, index, insert, pop, remove, reverse, sort

"""
#range function
#can be used to construct loops to go though lists

#equivalent loops

friends = ['Joseph','Glenn','Sally']

for friend in friends :  #simple is better! :-P
    print 'Happy New Year:',friend

for i in range(len(friends)) :  #using this value i allows you to change somthing in the list
    friend = friends[i]
    print 'happy new year:',friend 
    
# can concatenate lists using +
a = [1,2,3]
b = [4,5,6]
c = a + b 
print c

#slice lists kinda like strings
t = [9,41,12,3,74,15]
print t[1:3] #remember just like strings, second number is 'up to but not including'

# Building a List from Scratch!
x = list() # or x = []
x.append('book')
x.append(99)
x.append('cookie')
print x 

#Is an item in a list?
some = [1,9,21,10,16]
if 9 in some: #can also use 'not in'
    print True
    
# built in functions for lists
nums = [3,41,12,9,74,15]

#length of list
print len(nums)
#largest number
print max(nums)
#Min
print min(nums)
#sum
print sum(nums)
#average
print sum(nums)/len(nums)

#Exercise using lists do do averages -- this loop hold each number in a list might slow things down with millions of numbers
numlist = list()
while True: 
    inp = raw_input('Enter a number:')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print 'Average:',average     

# SPLITS! -- connecting strings and lists -- helps to begin parsing strings!
abc = 'with three words' #this is a string
stuff = abc.split() #split to a list
print stuff
print len(stuff) #how many values are in the list? 3
print 'the first value in the list is:' stuff[0]
#loop through
    for w in stuff :
        print w
# split sees many spaces as one space!!
line = 'A lot                 of spaces'
etc = line.split()
print etc
#can put a delimiter in split i.e. split(';') 