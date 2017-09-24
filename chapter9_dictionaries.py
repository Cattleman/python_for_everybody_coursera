"""
 @author: Hensel
 
 Chapter 9 - Dictionaries
 
 Source: https://www.coursera.org/learn/python-data/lecture/DqZWy/chapter-9-dictionaries
 
"""
 
 #collections 
    #List = a linear collection of values that stay in order
    #Dictionary is a bag of values, each with its own label, not in any order like a purse 
        #key /value - like a database 
        
purse = dict() #makes purse a dictionary
purse['Money'] = 12 # Money is the key (label) and 12 is the value in the purse dictionary
purse['candy'] = 3
purse['tissues'] = 75
print purse  # used {  } syntax when priting out a dictionary 

# Order is NOT preserved in dictionaries!

ddd = dict()
ddd['age'] = 21 # even though age is added 1st, the order isnt preserved 
ddd['course'] = 182
print ddd
ddd['age'] = 23 # this reassigns a value to that label
print ddd # the age label's value is changed to 23

# Dictionary Literals (constants)
jjj = {'chuck':1,'fred':32,'jan':100} #order isnt stored!
print 'jjj',jjj
ooo = {}
print 'ooo',ooo
#dictionaries are kind of like a histogram! 
#you can't reference a key when it doesnt exist!

print 'csev' in ccc # will return a bool (T/F)

#Even though dictionaries are not stored in order , we can write a for loop that goes 
#through all the enteries in a dicitonary - actually it goes through all the keys in the 
#dictionary and looks up the VALUES

#exsmple:
conts = {'chuck' : 1,'fred' : 42, 'jan' : 100}
for key in counts:
    print key, counts[key]

#RETRIEVING LISTS OF KEYS AND VALUES
#You can get a list of keys, values or items(both) from a dicitonary! 
jjj = {'chuck':1,'fred':32,'jan':100}
print 'jjj keys', jjj.keys()
print 'jjj values', jjj.values()
print 'jjj items', jjj.items() #items returns a list of 'tuples' a tuple is a key value pair
  