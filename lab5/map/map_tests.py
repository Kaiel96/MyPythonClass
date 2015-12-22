import unittest
from map import *
from point import *

class TestCases(unittest.TestCase):
   
   def test_square_1(self):
   	nums=[-3,-1,0,1,3]
   	self.assertListEqual(square_all(nums),[9,1,0,1,9])

   def test_square_2(self):
   	nums=[-5,-2,0,2,5]
   	self.assertListEqual(square_all(nums),[25,4,0,4,25])

   def test_add_n_1(self):
   	nums=[-1,0,3,5]
   	self.assertListEqual(add_n_all(nums,2),[1,2,5,7])

   def test_add_n_2(self):
   	nums=[-2,3.4,5.0]
   	self.assertListEqual(add_n_all(nums,3),[1,6.4,8.0])
   	
   def test_distance_1(self):
   	nums=[Point(3,4),Point(5,12)]
   	self.assertListEqual(distance_all(nums),[5,13])
   def test_distance_2(self):
   	nums=[Point(9,40),Point(-9,-40)]
   	self.assertListEqual(distance_all(nums),[41,41])






# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

