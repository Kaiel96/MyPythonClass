import unittest
from fold import *
from point import *

class TestSumCases(unittest.TestCase):
	def test_sum_1(self): 
		nums = [1,2,3]
		self.assertEqual(sum(nums),6)
	def test_sum_2(self):
		nums = [7,8,10]
		self.assertEqual(sum(nums),25)
		
class TestIndexCases(unittest.TestCase):
	
	def test_index_1(self):
		nums = [1,3,5,2,4]
		self.assertEqual(index_of_smallest(nums),0)
	
	def test_index_2(self):
		nums = [4,5,1,2,5]
		self.assertEqual(index_of_smallest(nums),2)

class TestOriginCases(unittest.TestCase):
	
	def test_near_origin_1(self):
		nums = [Point(1,2),Point(4,5)]
		self.assertEqual(nearest_origin(nums),0)

	def test_near_origin_2(self):
		nums = [Point(3,4),Point(1,1)]
		self.assertEqual(nearest_origin(nums),1)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

