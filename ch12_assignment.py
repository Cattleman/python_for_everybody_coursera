"""
@author: Hensel
9/6/16

Chapter 12 asignment: Scraping HTML Data with BeautifulSoup

"""
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
