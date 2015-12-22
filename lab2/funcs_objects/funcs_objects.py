import math
from objects import *

def distance (p1, p2):
   return math.sqrt(abs(p1.x-p2.x)**2+abs(p1.y-p2.y)**2)


def circles_overlap(c1,c2):
   return c1.radius +c2.radius > distance(c1.center, c2.center)
