import unittest
from string_101 import *

class TestString(unittest.TestCase):
   def test_str_rot(self):
   		self.assertEqual(str_rot_13('ab'),'no')
   def test_translate(self): 
   		self.assertEqual(str_translate_101('catan','c','b'),'batan')




if __name__ == '__main__':
   unittest.main()

