# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:16:54 2016

@author: Hensel

Averaging loop 

This loop averages the numbers in the set

"""

count = 0
sum = 0 

print 'before', count, sum
for value in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + value
    print count,sum,value
print 'After', count, sum, sum / count


"""
Boolean variable
 True or False


"""

found = False
print 'Before', found
for value in [9,41,12,3,74,15]:
    if value ==3:
        found = True
    print found, value
print 'After', found 