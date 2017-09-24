"""
@author: Hensel
8/31/16

Chapter 9: Most Common Name

"""
counts = dict()
names = ['csev','cwen','csev','zqian','cwen'] #a list!
for name in names :
    if name not in counts: #checks to see if it is in a dictionary
        counts[name] = 1 #if a name isnt in dictionary add it as a key /w value 1
    else:
        counts[name] = counts[name] + 1 #if the name is, add 1 to it's value
print counts         

#new method: get

if name in couts: 
    print counts[name]
else:
    print 0 
    
#Bellow = what is above     
print couts.get(name,0) #get has a key variable and a value variable to 
                        #enter if the key is not in dictionary    
                        
#put all together

counts = dict()
name = ['csev','cwen','csev','zqian','cwen']
for name in names :
    count[name] = count.get(name,0) + 1 # this will either create or update dictionary 
print counts     

