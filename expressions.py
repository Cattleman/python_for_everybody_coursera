#constant is a fixed value, strings are constants
#assignment satement

y = 14
x=1+2**3/4*5
print x #prints x current value
#numeric expression operators
# + Addition 
# - subtraction
# * multiplication
# / Division
# ** Power
# % remainder like from long division

#Type conversion

print float(99)/100
i =42

type(i)
<type 'int'>
f = float(i)
print f

type(f)
<type 'float'> #output from python
print 1+2*float(3)/4-5

#inputs and converts to int and adds then prints conversion 
inp = raw_input('Europe floor?')
usf = int(inp) + 1 
print "US floor", usf