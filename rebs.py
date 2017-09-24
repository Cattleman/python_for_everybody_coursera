
gos = raw_input('Ground or space? (0/1) ')

id = int(gos)

#calculate Ground combat dice
if id == 0 :
        t1 = int(raw_input('How many troopers? '))
        t2 = int(raw_input('How many ATSTs or Air Speeders? '))
        t3 = int(raw_input('How many ATATs? '))
        #black dice
        bd = (t1 * 1) + (t2 * 1) + (t3 * 1)
        #red dice calculation
        rd = (t2 * 1) + (t3 * 2 ) 
        print 'Roll Black: ', bd
        print 'Roll Red: ', rd
 
#calculate Space combat dice 
if id == 1 :
        s1 = int(raw_input('How many Xwing or Tie Fighters?'))
        s2 = int(raw_input('How many YWing or Assult Carriers?'))
        s3 = int(raw_input('How Many Corvets or StarDestroyers?'))

ask = raw_input('Auto Roll? (0/1) ')
ida = int(ask)

#random dice roll
bdr = [0, 1, 2, 3, 4]    

#def dice_roll()
    #random.choice(t)
   #page 48 of python pdf 
   #import random
#t = [0, 1, 2, 3, 4]    
#print random.choice(t)print random.choice(t)

     



#if ida == 0:
    import random
    #black die roll
    bdr = [0, 1, 2, 3, 4]
    #black dice damage
    bdd = bd * (random.choice(bdr))
    print bdd
#elif ask == 1:
    #print 'Blow on them dice boy!' 
    
        

    
