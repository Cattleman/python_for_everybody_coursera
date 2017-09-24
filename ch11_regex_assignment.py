"""
@author Hensel
9/6/16

Extracting Data with Regular Expressions 


Handling The Data
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.


"""

handle = open('regex_sum_309845.txt') # will need to change for asignment 

text = handle.read()
import re
numlist = list()
#print 'numlist type',type(numlist)
count = 0
y = list()

y = re.findall('[0-9]+',text )

for i in y:
    count = count + 1
    itgr = int(i)
    numlist.append(itgr)
print 'There are',count,'values with a sum =',sum(numlist)

    
#SHORTEST WAY

import re
print sum( [ int(i) for i in re.findall('[0-9]+',open('regex_sum_309845.txt').read()) ] )