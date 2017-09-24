"""
Week 7 Chapter 5 
Loop Idioms

"""

#looping through a set

print 'Before'
for thing in [9,41,12,3,74,15]:
    print thing
print 'After'    

#what is the Largest Number?

largest_so_far = -1
print 'Before', largest_so_far
for the_num in [9,4,12,3,74,15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print largest_so_far,the_num
print 'After', largest_so_far    

#Counting in a loop, add a counting varriable
zork = 0 #this will be our counting variable. it will be +1 each time through the loop
print 'Before', zork
for thing in [9,41,12,3,74,15]:
    zork = zork + 1  #add one each time through loop
    print zork, thing
print 'After', zork

#Summing in a loop. 'Running total'
york = 0 
print 'Before', york
for thing in [9,41,12,3,74,15]:
    york = york + thing
    print york, thing
print 'After', york

#Average in a loop