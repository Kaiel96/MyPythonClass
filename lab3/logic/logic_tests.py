import unittest
from logic import *

class Test_even_cases(unittest.TestCase):

   def test_is_even_1(self):
      self.assertTrue(is_even(4))

   def test_is_even_2(self):
      self.assertFalse(is_even(5))

class Test_interval_inclusion(unittest.TestCase):

   def test_in_interval_1(self):
      self.assertFalse(in_an_interval(9))

   def test_in_interval__2(self):
      self.assertTrue(in_an_interval(50))

   def test_in_interval__3(self):
      self.assertTrue(in_an_interval(19))

   def test_in_interval__4(self):
      self.assertTrue(in_an_interval(103))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

