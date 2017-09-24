"""
@author: hensel 8/29/16

7.1 Write a program that prompts for a file name, then opens that file and reads through the file, 
and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.pythonlearn.com/code/words.txt


"""

# Use words.txt as the file name
fname = raw_input('Enter the file Name: ')
try:
    fhand = open(fname)
except:
    print 'File cannot be found:',fname
    exit()
    
inp = fhand.read() #reads whole file    
stp = inp.strip() #strips extra \n 
opt = stp.upper() #converts the stripped string to uppercase
print opt
    
