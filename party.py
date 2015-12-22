print "Age:",
age = int(raw_input())

print "Do You like Music?:",
like_music= raw_input() == "yes"

if answer == "yes":
    like_music = True
else:
    like_music= False

if age>28:
       print "get lost gramps!"

elif age >= 18 and age <=28:
    if like_music == True:
       print "you're invited"
    else:
        print "you're dead to me."
        

else:
       print "you want a lollipop kid? SCRAM!"

