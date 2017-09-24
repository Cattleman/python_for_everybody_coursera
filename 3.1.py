hrs = raw_input("enter Hours:")
h = float(hrs)

rate = raw_input("Enter Rate: ")
r = float(rate)

#need a value to pay up to 40 hrs
pay = 40.0 * r

if h <= 40.0:
    bp = h * r
    print bp

if h > 40.0:
    #over time calc
        ot = float((h - 40.0))
        otr = float(r * float(1.5))
        otp = float(ot * otr)
     #add ot and base
        totpay = float( otp + pay )
        print totpay