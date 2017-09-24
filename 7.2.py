"""
@author Hensel
8/29/16

7.2 assignment

promt for file
counts lines in for 'X-DSPAM-Confidence: 0.8475'
extract the floating point value and computes average to produce an average value 
"""

fname = raw_input('Enter file name: ')
count = 0. # used 0. to have it be float value
rtot = 0.
if len(fname) == 0: #this allows me to press enter to skip entering the file name - shortcut!
    fname = 'mbox-short.txt'
try:
    fh = open(fname) 
except: 
    print 'Cant find file'
    exit()
    
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:') :  #if not is used to have loop continue through text
        continue #starts next iteration
    if line.startswith('X-DSPAM-Confidence:') : 
        count = count + 1 #keeps track of number of times we have our search string
        num = line[21:] #this line takes 21st value in the string to the end 
        num_float = float(num) #convert from string to float
        rtot = float(num_float + rtot) #rolling total of spam conf values
avg = rtot / count #averages values       
    
print 'Average spam confidence:', avg    
    
