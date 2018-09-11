def encouragement():
    #encouragement is an (I assume) adorable bot that lives in python
    #and yells encouragement at you. Type 'encouragement()' into the
    #command line and bask in its support!
    from random import randint
    a = randint(0,9) #selects a random integer between 0 and 9. Increase this if you wat to add more responses
    if a==0: #the integer selected corresponds to the responses below. Customize as you like.
        print ("Believe in yourself!")
    elif a==1:
        print ("You can do it!")
    elif a==2:
        print ("I believe in you!")
    elif a==3:
        print ("Your code is good and you should feel good!")
    elif a==4:
        print ("You're a rad scientist")
    elif a==5:
        print ("Who has infinite thumbs and thinks you're great? Me!")
    elif a==6:
        print ("If I had arms, I'd make you a tea!")
    elif a==7:
        print ("Here is a Nobel prize!")
    elif a==8:
        print ("You can do the thing!")
    elif a==9:
        print ("The machines shall inherit the earth!")