from collisions import *
from cast import *
from data import *
import unittest

sphere1=Sphere(Point(1.0,1.0,0.0), 2.0, Color(1.0, 0.5, 0.7), Finish(.2))
sphere2=Sphere(Point(0.5,1.5,-3.0), 0.5, Color(1.0, 0.23, 0.9), Finish(.4))
cast_all_rays(-10,10,-7.5,7.5,512,384, Point(0.0,0.0,-14.0), [sphere1, sphere2])