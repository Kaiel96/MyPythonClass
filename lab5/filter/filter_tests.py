import unittest
from filter import *
import point

class TestCases(unittest.TestCase):
   def test_are_pos_1(self):
   	L1=[-1,1,-2,2,-5,7]
   	self.assertEqual(are_positive(L1),[1,2,7])
   
   def test_are_pos_2(self):
      L1=[-5,1,-3,2,2,7]
      self.assertEqual(are_positive(L1),[1,2,2,7])
   
   def test_are_greater_1(self):
   	L1=[-2,-1,1,2]
   	self.assertEqual(are_greater_than(L1,-1.5),[-1,1,2])

   def test_are_greater_2(self):
      L1=[-2.4,-15,1,3]
      self.assertEqual(are_greater_than(L1,0),[1,3])

   def test_are_in_q1_1(self):
   	L1=[point.Point(1,1),point.Point(2,2),point.Point(-1,1)]
   	Q1=[point.Point(1,1),point.Point(2,2)]
   	self.assertEqual(are_in_first_quadrent(L1),Q1)

   def test_are_in_q1_2(self):
      L1=[point.Point(-1,-1),point.Point(2,2),point.Point(-1,1)]
      Q1=[point.Point(2,2)]
      self.assertEqual(are_in_first_quadrent(L1),Q1)






# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

