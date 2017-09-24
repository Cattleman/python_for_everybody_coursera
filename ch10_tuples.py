"""
@author: Hensel

9/1/16 

Chapter 10 Tuples!
"""

#Tuples are another kind of sequence that function much like a list
#they have elements which are indexed starting at 0
#Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string!
#Tuples are 'immutable' (unlike lists) ALSO cant sort, reverse

#Tuples are a reduction of what we can do than in lists, this makes them more efficent becuase python knows we cant change them
#tuples are prefered for temporary variables 

# can put tuples on the left side of an assignment statement

(x,y) = (4, 'fred')
print y
#returns 'fred'
(a,b) = (99,98)
print a
#returns '99'

a,b = (99,98) # no parenthesis is ok 

#TUPLES AND DICTIONARIES 
#the items() method in dictionaries returns a list of (key, value) tuples

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items(): 
    print k,v 
#returns csev 2 and cwen 4

tups = d.items()
print tups
#returns a list of tuples 

#TUPLES are COMPARABLE 
(0, 1, 2) < (5, 1, 2)
#returns True   looks at left most value 1st if = contiues
#can also do strings
('Jones', 'Sally') > ('adam', 'sam')

#we can take advantage of the ability to sort a list of tuples to get a sorted version of a dicitonary
#1st we sort the dictionary by the key using the items() method
d = {'a':10, 'b':1, 'c':22} #dictionary 
t = d.items() #returns a list of tuples
t.sort() #way to sort by keys
print t.sort() #returns a sorted list of tuples (a,b,c)

##Built in function sorted() - We can do the above even more directly using the built-in function sorted() that takes a sequence
#as a parameter and renturns a sorted sequence 

for k,v in sorted(d.items()) : #loop will run in key sorted order
    print k, v
    
##SORTING BY VALUES INSTEAD OF KEY 
#construct a list of tuples of the form(value,key) we could sort by value
#use a for -loop that creates a list of tuples 
c = {'a':10, 'b':1, 'c':22}
tmp = list() #temporary list 
for k,v in c.items(): #loop through dictionary and change the order of value 
    tmp.append((v,k)) #make a two tuple with the v,k variables 
print tmp
tmp.sort(reverse=True) #sort from highest to lowest 
print tmp     

#LIST COMPREHENSION

c = {'a':10, 'b':1, 'c':22}
print sorted( [ (v,k) for k,v in c.items() ] ) 
#list comperehinesion - python syntax, create a list of tuples in (v,k) order
 
