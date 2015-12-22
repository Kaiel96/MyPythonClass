import unittest
import vehicle

class VehicleTests(unittest.TestCase):
   def test_vehicle(self):
      # Add code here.
    test1=vehicle.Vehicle(4,8.7, 2,False)
    self.assertEqual(4, test1.wheels)
    self.assertEqual(8.7, test1.fuel)
    self.assertEqual(2, test1.doors)
    self.assertEqual(False, test1.roof)
   def test_vehicle2(self):
    test2=vehicle.Vehicle(8, 16.8, 4, True)
    self.assertEqual(8, test2.wheels)
    self.assertEqual(16.8, test2.fuel)
    self.assertEqual(4,test2.doors)
    self.assertEqual(True,test2.roof)
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

