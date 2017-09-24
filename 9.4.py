"""
author: hensel
8/31/16

9.4 Assignment 

9.4 Write a program to read through the mbox-short.txt and figure out 
who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines 
as the person who sent the mail. The program creates a Python dictionary that 
maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

"""

fname = raw_input("Enter file:") #prompts user for input
if len(fname) < 1 : fname = 'mbox-short.txt' #allows us to skip entering the file 
try:
    handle = open(fname,'r') #open file and read 'r'
except:
    print 'File cannot be found.',fname
    exit()
 
email_dict = dict() #establish email dictionary 
count = 0
email_list = list()

for line in handle : #goal of loop: find only lines wiht 'From ' 
    if not line.startswith('From '): continue #skips lines that dont start with 'From ' 
    #if from_list == [] : continue #gaurdian pattern - do somthing before the line that breaks. if words is an empty list, continue
    #if from_list[0] != 'From' : continue
    if line.startswith('From '):
        from_list = line.split() # splits each string into a list 
        email_list.append(from_list[1]) #moves the 2nd string from each line into email_list
        
for email in email_list : #takes strings in email_list and makes the emails keys in the dictionary
    email_dict[email] = email_dict.get(email,0) + 1 #this will either create or update dictionary      
#print email_dict -- used to trouble shoot   
#Now that we have emails and the count in a dictionary we want to sort the most common sender and number of emails they sent       
big_commit = None #define terms 
big_count = None    
     
for email,count in email_dict.items(): #two value iterative pair email = key, count = value
    if big_count is None or count > big_count:
        big_commit = email #change the key to the biggiest committer so far
        big_count = count #change the count to the largest count so far

print big_commit,big_count            
