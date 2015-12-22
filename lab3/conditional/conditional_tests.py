import unittest
from conditional import *

class Max101Cases(unittest.TestCase):

   def test_max_101__1(self):
      self.assertEqual(max_101(1,2),2)

   def test_max_101_2(self):
      self.assertEqual(max_101(7,3),7)

class Max_3_Cases(unittest.TestCase):
      
   def test_max_of_three_1(self):
      self.assertEqual(max_of_three(3,2,1),3)

    
   def test_max_of_three_2(self):
      self.assertEqual(max_of_three(2,3,1),3)
    
   def test_max_of_three_3(self):
      self.assertEqual(max_of_three(1,2,3),3)

class Rentals_test_cases(unittest.TestCase):

   def test_rental_late_fee__1(self):
      self.assertEqual(rental_late_fee(0),0)

   def test_rental_late_fee__2(self):
      self.assertEqual(rental_late_fee(9),5)

   def test_rental_late_fee__4(self):
      self.assertEqual(rental_late_fee(15),7)
      
   def test_rental_late_fee__5(self):
      self.assertEqual(rental_late_fee(24),19)
   
   def test_rental_late_fee__6(self):
      self.assertEqual(rental_late_fee(40),100)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

