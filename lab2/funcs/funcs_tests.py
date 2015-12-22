import unittest
import funcs

class TestCases(unittest.TestCase):
   def test_f_1(self):
      # Add code here.
      self.assertEqual(funcs.f(-1),5)

   def test_f_2(self):
      self.assertEqual(funcs.f(2),32)

   def test_g_1(self):
      self.assertAlmostEqual(funcs.g(1,1),0.66666666)

   def test_g_2(self):
      self.assertAlmostEqual(funcs.g(3,4),2.7777777777)
   
   def test_hypt_1(self): 
      self.assertEqual(funcs.hypotonuse(3,4),5)
      
   
   def test_hypt_2(self):
      self.assertEqual(funcs.hypotonuse(5,12),13)
   
   def test_is_pos_1(self):
      self.assertTrue(1,True)
   
   def test_is_pos_2(self):
      self.assertTrue(-1,False)

      # Add code here.
  
     

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

