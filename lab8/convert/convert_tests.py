import unittest
from convert import *

class TestConvert(unittest.TestCase):
   def test_convert(self):
      self.assertTrue(float_default('50',5) == 50.0)
   def test_convert_2(self):
   		self.assertTrue(float_default('sandwich',6) == 6)

class Test



if __name__ == '__main__':
   unittest.main()

