#classic if then else for week 5 conditional execution

hrs = float(raw_input('Enter your hours: '))

rate = float(raw_input('enter your rate: '))

ovrt = float(raw_input('enter your overtime rate: '))

if hrs > 40:
    ovr = float(hrs - 40) 
    
    opay = float(ovr * ovrt)
    totpay = float(opay + (hrs * rate))
   
    print totpay
    
else: 
    pay = rate * hrs
    print 'your pay: ', pay