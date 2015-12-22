import unittest
from funcs_objects import *

class TestCases(unittest.TestCase):

   def test_point(self):
      p1=Point(1,2)
      self.assertEqual(p1.x,1)
      self.assertEqual(p1.y,2)

   def test_point_2(self):
      p2=Point(2,3)
      self.assertEqual(p2.x,2)
      self.assertEqual(p2.y,3)

   def test_circle(self):
      c1=Point(-1,2)
      self.assertEqual(c1.x,-1)
      self.assertEqual(c1.y,2)

   def test_circle_2(self):
      c2=Point(-2,4)
      self.assertEqual(c2.x,-2)
      self.assertEqual(c2.y,4)

   def test_distance(self):
      p1=Point(1,4)
      p2=Point(1,0)
      self.assertEqual(distance(p1,p2),4)

   def test_distance_2(self):
      p1=Point(2,6)
      p2=Point(2,2)
      self.assertEqual(distance(p1,p2),4)
   

   def test_circle_overlap(self):
      c1=Circle(Point(0,0),1)
      c2=Circle(Point(2.1,0),1)
      self.assertFalse(circles_overlap(c1,c2))
   

   def test_circles_overlap_2(self):
      c1=Circle(Point(0,0),1)
      c2=Circle(Point(1.4,1.4),1)
      self.assertTrue(circles_overlap(c1,c2))
   
      
   # Add other testing functions


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

