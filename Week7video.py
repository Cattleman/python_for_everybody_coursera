""" 
@Hensel
week 7 Chapter 5  - Loops and Iterations!
video for 5.1: loops and iterations

Notes:
uses 'while' keyword
do code in indented block or skip it. 
'while' is similar to 'if' except 'while' will do it over and over rather than once
#Definite loops -- uses keyword 'for'

"""

n = 5

while n > 0:
    print n
    n = n - 1
print 'Blast off!'
print n     

#common problem is an infinte loop. if a value doesnt change, loop will never exit. 
#value must change to have loop end eventually.

#Breaking out of a loop
#the break statment ends the current loop and jumps to the satement immeditely following the loop
#it is like a loop test that can happen anywhere in the bod of the loop
#'break' allows python to escape the loop and execute the next line. "A jump to the next line"

while True:
    line = raw_input('>')
    if line == 'done':
        break
        print line
print 'Done!'       

#if line[0] == '#':
    #continue < == this ends the iteration of the loop and starts over
    
while True:
        line = raw_input('>')
        if line[0] == '#':
           continue
        if line == 'done':
            break
        print line 
print 'Done!'        

#loops made with 'while' keyword are indefinte loops b/c they keep going until condition is false
#Definite loops -- uses keyword 'for'
# 'for' loop advances the iteration variable 

for i in [5,4,3,2,1]: # run this loop for each value / cycle through these
    print i 
print 'Blastoff!'

friends = ['Joseph','Glenn','Sally']

for friends in friends:
    print 'Happy New Year:', friends
print 'Done!'