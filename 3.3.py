
score = raw_input('Enter Score: ')

try: 
    s = float(score)
    if s > 1.0:
        print 'Please enter a score between 0.0 and 1.0'
    elif s >= 0.9 and s <= 1.0:
        print 'A'
    elif s >= 0.8 and s < 0.9:
        print 'B'
    elif s >= 0.7 and s < 0.8:
        print 'C'
    elif s >= 0.6 and s < 0.7:
        print 'D'
    elif s < 0.6:
        print 'F'
        
except:
    print 'Please enter a score between 0.0 and 1.0'
    quit()

