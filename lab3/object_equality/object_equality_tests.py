import unittest
import point
from utility import *

class TestCases(unittest.TestCase):
   def test_point_one(self):
      pt = point.Point(1, 2)
      self.assertAlmostEqual(pt.x, 1)
      self.assertAlmostEqual(pt.y, 2)


   def test_point_two(self):
      pt = point.Point(-4.7, 19.2)
      self.assertAlmostEqual(pt.x, -4.7)
      self.assertAlmostEqual(pt.y, 19.2)


   def test_equality(self):
      p1=point.Point(1,2)
      p2=point.Point(1,2)
      self.assertTrue(p1==p2)

   def test_equality_2(self):
      p1=point.Point(2,3)
      p2=point.Point(4,5)
      self.assertFalse(p1==p2)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

