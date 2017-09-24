# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 12:39:45 2016

@author: Hensel
 Write code using find() and string slicing (see section 6.10) 
 to extract the number at the end of the line below.
 Convert the extracted value to a floating point number and print it out.

"""

text = "X-DSPAM-Confidence:    0.8475"

colon = text.find(':')
#print colon
numstr = text[colon+1:] # using :] just makes range to the end!
num = numstr.strip()
#print num
digit = float(num) # can also use whole expression text[colon+1:]
print digit, type(digit)

"""
number = text.find(' )

num_string = text[colon,]

data = 'From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print atpos
sppos = data.find(' ',atpos) #find a blank starting at the atpos value
print sppos
host = data[atpos+1:sppos] #slicing operation start at atpos (dont want to include so +1) then go to sppos
print host  # this is called parsing Text 
"""