import unittest
import poly

class TestPoly(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)


   # Add tests here


def test_poly_add2:
   poly1=[2.3,3.4,4.6]
   poly2=[2.7,1.6,.5]
   poly3=poly1+poly2
   self.assertListAlmostEqual(poly3, [5.0, 5.0,5.1])

def test_poly_mult2:
   poly1=[2.0,3.0,2.0]
   poly2=[2.7,1.6,.5]
   poly3=poly1*poly2
   self.assertListAlmostEqual(poly3, [5.0, 5.0,5.1])





if __name__ == '__main__':
   unittest.main()
