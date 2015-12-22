import unittest 
import line

class LineTests(unittest.TestCase):
   def test_line(self):
      test_1 = line.Line(1000, 65, 34.9, 4.0)
      self.assertEqual(1000, test_1.x1)
      self.assertEqual(65, test_1.y1)
      self.assertEqual(34.9, test_1.x2)
      self.assertEqual(4.0, test_1.y2)
   def test_line2(self):
      test2= line.Line(57, 38.96, -48, 13.6)
      self.assertEqual(57, test2.x1)
      self.assertEqual(38.96, test2.y1)
      self.assertEqual(-48, test2.x2)
      self.assertEqual(13.6, test2.y2)
      # Add code here.
      # 1) Create a Line with x1, y1, x2, y2 values of your choice.
      # 2) Use assertEqual on each field in the new Line to verify
      #    that it holds the expected value.


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

