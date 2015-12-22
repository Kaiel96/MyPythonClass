from timer import *


t1=Time(8,43,12)
t2=Time(9,18,55)

timer1=Timer(t1,t2)
timer2=Timer(Time(1,2,3), Time(4,5,6))
print timer2.stopTime.h,timer2.stopTime.m,timer2.stopTime.s


