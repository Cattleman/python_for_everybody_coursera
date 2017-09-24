#try and except practice from lecture 3.3 in week 5
#try and except pairs

astr = 'hello Bob'
try:
    istr = int(astr)
except:
    istr = -1

print 'Done', istr

#check an input value bellow

rawstr = raw_input('Enter a number:')

try:
    ival = int(rawstr) #converts to intiger or blows up
except:
    ival = -1

if ival > 0:
    print 'Nice work'

else:
    print 'Not a number'
    