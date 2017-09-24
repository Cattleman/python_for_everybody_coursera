"""
@author: hensel
9/6/2016
Chapter 12: Programs that Surf the Web!
"""

#UNDERSTANDING HTML
#Web scraping - app that pretends to be a browser and grabs wanted info
#DIFF sites have diff stances for scraping - be careful 


#Parsing HTML with BeautifulSoup for python 2.0

import urllib 
from BeautifulSoup import *  #brings in whole libary 

url = raw_input('Enter - ')

html = urllib.urlopen(url).read() #read it all! we get a string of the whole web page 
soup = BeautifulSoup(html) #feed BS whole string of the page 
#soup = object for us to manupulate
#Retrieve a list of the anchor tags
#each tag is like a dictionary of HTML attributes

tags = soup('a') #finds <a "A tags" usually for links <a href = "blahbhah.com"

for tag in tags:
    print tag.get('href', None)


# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

"""
BEAUTIFUL SOUP STUFFF!
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print 'TAG:',tag
    print 'URL:',tag.get('href', None)
    print 'Contents:',tag.contents[0]
    print 'Attrs:',tag.attr
"""  