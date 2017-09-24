""" 
largest and smallest values

5.3 video
@Hensel
"""
largest_so_far = None #None is a special value. It isnt a number. It is a diff. type
smallest_so_far = None

#print 'Before', smallest_so_far

for the_num in [9,41,12,3,74,15]:
    if smallest_so_far is None: #triggers on 1st itteration. 'is' can be useful, but use only with special values 
        smallest_so_far = the_num
    elif the_num < smallest_so_far: #when to keep
        smallest_so_far = the_num #keep if smaller
    if largest_so_far is None:
        largest_so_far = the_num
    elif the_num > largest_so_far:
        largest_so_far = the_num
    print smallest_so_far,largest_so_far

print 'After',smallest_so_far,largest_so_far
    