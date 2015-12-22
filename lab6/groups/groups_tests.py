import unittest
from groups import group_of_3

class TestGroupsCases(unittest.TestCase):

	def test_groups_test_1(self):
		nums = [1,2,3,4,5,6]
		self.assertEqual(group_of_3(nums),[[1,2,3],[4,5,6]])
	
	def test_groups_test_2(self): 
		nums = [2,4,6,8,10,12,14,16,18]
		self.assertEqual(group_of_3(nums),[[2,4,6],[8,10,12],[14,16,18]])

   # Add tests here

if __name__ == '__main__':
   unittest.main()
