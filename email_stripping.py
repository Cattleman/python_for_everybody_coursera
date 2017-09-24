# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 12:31:00 2016

@author: Hensel
"""

data = 'From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print atpos
sppos = data.find(' ',atpos) #find a blank starting at the atpos value
print sppos
host = data[atpos+1:sppos] #slicing operation start at atpos (dont want to include so +1) then go to sppos
print host  # this is called parsing Text 