import unittest
from exam2 import *

class Test(unittest.TestCase):
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)
         
   def test_negatives(self):
      self.assertEqual(negatives([-8, 34, 75, 0, -3, -20]), [-8, -3, -20])
      
   def test_count_char(self):
      self.assertEqual(count_char('hyaawCbaEBAA', 'a'), 3)
      
   def test_find_max_index(self):
      self.assertEqual(find_max_index([22, -3, 78]), 2)

   def test_age_tally(self):
      self.assertEqual(age_tally([100, 77, 18, 12, 64, 65]), (1, 2, 3))

   def test_float_range(self):
      self.assertListAlmostEqual(float_range(1, 3), [1, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8])

      
if __name__ == '__main__':
   unittest.main()
