"""
@Hensel

5.2 assignment: Loops

"""
#largest = largest_1
#smallest = smallest_1

largest_so_far = None #None is a special value. It isnt a number. It is a diff. type
smallest_so_far = None

#def maxormin():
    #print "max", largest_so_far
    #print "min", smallest_so_far

    
while True:
    num = raw_input("enter a number ")
    if num == 'done' : break    #break jumps to the code imediatly outside the loop    
    #if len(inp) < 1 : break # check for empty line    
    try: 
        the_num = int(num) 
        
        if smallest_so_far is None: #triggers on 1st itteration. 'is' can be useful, but use only with special values 
            smallest_so_far = the_num
            print smallest_so_far
        elif the_num < smallest_so_far: #when to keep
            smallest_so_far = the_num #keep if smaller
            print 'smallest so far', smallest_so_far
        
    if largest_so_far is None:
        largest_so_far = the_num
    elif the_num > largest_so_far:
        largest_so_far = the_num
        print 'largest',largest_so_far
        
    #print smallest_so_far,largest_so_farcontinue
    except:
        print 'invalid input'
       
    
    


#max_min()
print 'max', largest_so_far
print 'min', smallest_so_far
#quit()

   
#except:
    #print "Invalid input" 



"""
for the_num in [9,4,12,3,74,15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print largest_so_far,the_num
print 'After', largest_so_far    

"""