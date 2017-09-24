import re
import urllib 
from BeautifulSoup import *  #brings in whole libary 

url = raw_input('Enter - ') #http://python-data.dr-chuck.net/comments_42.html

html = urllib.urlopen(url).read() #read it all! we get a string of the whole web page 
soup = BeautifulSoup(html) #feed BS whole string of the page 
#soup = object for us to manupulate
#Retrieve a list of the anchor tags
#each tag is like a dictionary of HTML attributes

tags = soup('span') #finds <a "A tags" usually for links <a href = "blahbhah.com" /a>

count = 0
x = 0
for tag in tags:
   # Look at the parts of a tag
    if tag.contents[0] > 0:
        count = count + 1 
        x = x + (int(tag.contents[0]))
print 'count', count  
print 'sum', x

"""
count = 0
y = list()
#y.append(tag in tags)
#print tags #give list of <span> tags 
print 'type for tags', type(tags)
print 'list item type', type(tags[0]) #class issue where the items in the list are not str!

for tag in tags:
    y.append(str(tag))

for i in y: 
    x = re.findall('[0-9]+', y)
    print x 
#print 'y type', type(y)
#print 'yitem type', type(y[0])
   
x = re.findall('[0-9]+', y)
print x

#print tags
for tag in tags : 
    try:
        x = re.findall('[0-9]+', tags)
    except: continue
        
print x 



#print 'sum', sum( [ int(i) for i in re.findall('[0-9]+',y) ] )

#print sum( [ int(i) for i in re.findall('[0-9]+',open('regex_sum_309845.txt').read()) ] )

"""