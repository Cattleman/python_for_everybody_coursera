"""
4.6 assignment 
"""

hrs = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate: ")

h = float(hrs)
r = float(rate)

def computepay(h,r):
    if h > 40:
        ot = (h - 40) * (r * 1.5)
        otp = float(ot) + (40 * r)
        return otp
    else:
        rp = h * r
        return rp
    
p = computepay(h,r)    
print "Pay: ",p