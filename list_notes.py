
#mutable: can be changed

L1= [2,10,8.9,"look"]
print L1

print L1[1]

#This will return the second item in the list because lists start with 0

print L1[4]


#this will return an error because out of range

print L1[-1]

#This will return the rightmost spot

L2= ['ice','cream','stogies','hoagies']

L3=L1+L2

print L3

#This will return combination

L4=L1*10

print L4

#this will repeat the list in the list

L1[1]='cookies'
print L1

#This will replace spot 1 with cookies

L1[4]
print L1

#not gonna do shit

L1.append('dough')
print L1

#this will add 'dough' to the list

L1.pop(4)
#this will remove the item in the 4th spot
print L1

L1.remove('dough')

100 in L1
#test to see if item is in your list

len(L1)

#order matters in comparisions




1=(1,5,'burgers','fries')

#tuples are immutable(not changeable)

def int_div(x,y):
   q = x/y
   r = x%y
   return (q, r)

result = int_div(19,5)
print result

import math

def my_sqrt(x):
    if x<0:
        return None
    return math.sqrt(x)

def say_hello(first,last, mid = None):
	if mid != None:
            print ("Hello " +first+" "+mid+" "+ last)
        else:
            (print "Hello " +first+" "+ last)
