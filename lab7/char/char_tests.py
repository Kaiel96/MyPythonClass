import unittest
from char import *

class TestChar(unittest.TestCase):
   
   def test_lower_1(self):
   		self.assertTrue(is_lower_101('b'))
   def test_lower_2(self): 
   		self.assertFalse(is_lower_101('Z'))

class TestRot(unittest.TestCase): 
	def test_rot_1(self): 
		self.assertEqual(char_rot_13('a'),'n')
	def test_rot_2(self):
		self.assertEqual(char_rot_13('N'),'A')

	unittest.main()

