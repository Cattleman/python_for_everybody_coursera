"""
@author Hensel
9/2/16

Assignment 10.2

"""
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
#text = handle.read()

time_list = list()
hr_dict = dict()
hr_list = list()
hrs = list()
lst = list()
for line in handle : #goal of loop: find only lines wiht 'From ' 
    if not line.startswith('From '): continue #skips lines that dont start with 'From ' 
    #if from_list == [] : continue #gaurdian pattern - do somthing before the line that breaks. if words is an empty list, continue
    #if from_list[0] != 'From' : continue
    if line.startswith('From '):
        from_list = line.split() # splits each string into a list 
        #print from_list[5] #will print the time stamp
        #email_list.append(from_list[1]) #moves the 2nd string from each line into email_list
        time_list.append(from_list[5]) #makes a new list of time stamps 
#print time_list 
#print 'type', type(time_list[1]) #the hr_list is a list of strings so we can split agian

for times in time_list:
    hr_list = times.split(':') 
    hrs.append(hr_list[0])   #pupulates list 'hrs' with just the hour of the time stamps  
    
for hour in hrs: #each hour is a key 
    hr_dict[hour] = hr_dict.get(hour,0) + 1 #creates or increments the value of each key

#print sorted(hr_dict.items()) #sorts the tuples in the dictionary from smallest to largest
for key, val in sorted(hr_dict.items()): #take from the dictionary and append the hrs list 
    lst.append( (key, val) )
    print key, val



