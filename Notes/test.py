import unittest
import data

class PointTests(unittest.TestCase):
   def test_point(self): 
      test1 = data.Point(120, -45.6, 1000)   
      self.assertEqual(120, test1.x)
      self.assertEqual(-45.6, test1.y)
      self.assertEqual(1000, test1.z)
      test2 = data.Point(100,-64,2.5)
      self.assertEqual(100, test2.x)
      self.assertEqual(-64, test2.y)
      self.assertEqual(2.5, test2.z)

class VectorTest(unittest.TestCase):
   def test_vector(self):
      test3 = data.Vector(378.5, -56, 0.5)
      self.assertEqual(378.5,test3.x)
      self.assertEqual(-56,test3.y)
      self.assertEqual(0.5,test3.z)
      test4 = data.Vector(200, -5.5, 2)
      self.assertEqual(200,test4.x)
      self.assertEqual(-5.5,test4.y)
      self.assertEqual(2,test4.z)
      
class RayTests(unittest.TestCase):
   def test_ray(self):

      test5 = data.Ray(data.Point(2,3,1),data.Vector(3,1,2))
      self.assertEqual(data.Point(2,3,1).x, test5.pt.x)
      self.assertEqual(data.Point(2,3,1).y, test5.pt.y)
      self.assertEqual(data.Point(2,3,1).z, test5.pt.z)
      self.assertEqual(data.Vector(3,1,2).x, test5.dir.x)
      self.assertEqual(data.Vector(3,1,2).y, test5.dir.y)
      self.assertEqual(data.Vector(3,1,2).z, test5.dir.z)

      test6 = data.Ray(data.Point(4,5,6),data.Vector(7,8,9))
      self.assertEqual(data.Point(4,5,6).x, test6.pt.x)
      self.assertEqual(data.Point(4,5,6).y, test6.pt.y)
      self.assertEqual(data.Point(4,5,6).z, test6.pt.z)
      self.assertEqual(data.Vector(7,8,9).x, test6.dir.x)
      self.assertEqual(data.Vector(7,8,9).y, test6.dir.y)
      self.assertEqual(data.Vector(7,8,9).z, test6.dir.z)

class SphereTests(unittest.TestCase):
   def test_sphere(self):
      test7 = data.Sphere(data.Point(5,4,1),5)
      self.assertEqual(data.Point(5,4,1).x, test7.center.x)
      self.assertEqual(data.Point(5,4,1).y, test7.center.y)
      self.assertEqual(data.Point(5,4,1).z, test7.center.z)
      self.assertEqual(5, test7.radius)
      test8 = data.Sphere(data.Point(1,4,5),3)
      self.assertEqual(data.Point(1,4,5).x, test8.center.x)
      self.assertEqual(data.Point(1,4,5).y, test8.center.y)
      self.assertEqual(data.Point(1,4,5).z, test8.center.z)
      self.assertEqual(3, test8.radius)
                       
if __name__== '__main__':
   unittest.main()
