"""
@author: Hensel

8/30/16

Assignment 8.4 : lists

8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
 The program should build a list of words. For each word on each line check to see if the word is already in the list,
 if not append it to the list.
 When the program completes, sort and print the resulting words in alphabetical order.

"""
fname = raw_input("Enter file name: ")
if len(fname) == 0: #this allows me to press enter to skip entering the file name - shortcut!
    fname = 'romeo.txt'
try:
    fh = open(fname)
except:
    print 'File cannot be found.',fname
    exit()

dalist = list()

for line in fh:
    stp = line.rstrip() #strips each line of extra spaces
    #print stp
    splt = stp.split() # splits each line string into lists
    for i in splt:      # for variable 'i' in the list abc, , 
        if i not in dalist: #if 'i' is not in dalist
            dalist.append(i) #add i to the list, with this method we dont need to concatinate lists 
    dalist = sorted(dalist)  #sort the list alphabetically each time through the loop     
                           
    
    
print dalist   
