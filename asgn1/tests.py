import unittest
from data import *
import math
from vector_math import*

class PointTests(unittest.TestCase):

   def test_point_1(self): 
     
      p = Point(120, -45.6, 1000)   
      self.assertEqual(120, p.x)
      self.assertEqual(-45.6, p.y)
      self.assertEqual(1000, p.z)
   def test_point_2(self):
     
      p = Point(100,-64,2.5)
      self.assertEqual(100, p.x)
      self.assertEqual(-64, p.y)
      self.assertEqual(2.5, p.z)

   def test_point_equality1(self):
      p1 = Point(2, 3, 4)
      p2 = Point(2, 3, 4)
      self.assertTrue(p1 == p2)
      
   def test_point_equality2(self):
      p1 = Point(2, 3, 4)
      p2 = Point(5,6, 7)
      self.assertFalse(p1 == p2)



class VectorTest(unittest.TestCase):

   def test_vector_1(self):
     
      v = Vector(378.5, -56, 0.5)
      self.assertEqual(378.5,v.x)
      self.assertEqual(-56,v.y)
      self.assertEqual(0.5,v.z)
   
   def test_vector_2(self):

      v = Vector(200, -5.5, 2)
      self.assertEqual(200,v.x)
      self.assertEqual(-5.5,v.y)
      self.assertEqual(2,v.z)

   def test_vector_equality1(self):
      v1 = Vector(2, 3, 4)
      v2 = Vector(2, 3, 4)
      self.assertTrue(v1 == v2)
      
   def test_vector_equality2(self):
      v1 = Vector(2, 3, 4)
      v2 = Vector(5,6, 7)
      self.assertFalse(v1 == v2)


      
class RayTests(unittest.TestCase):

   def test_ray_1(self):

      ray = Ray(Point(2,3,1), Vector(3,1,2))
      p=Point(2,3,1)
      v=Vector(3,1,2)
      self.assertEqual(p.x, ray.pt.x)
      self.assertEqual(p.y, ray.pt.y)
      self.assertEqual(p.z, ray.pt.z)
      self.assertEqual(v.x, ray.dir.x)
      self.assertEqual(v.y, ray.dir.y)
      self.assertEqual(v.z, ray.dir.z)

   def test_ray_2(self):   
      
      ray = Ray(Point(4,5,6),Vector(7,8,9))
      p=Point(4,5,6)
      v=Vector(7,8,9)
      self.assertEqual(p.x, ray.pt.x)
      self.assertEqual(p.y, ray.pt.y)
      self.assertEqual(p.z, ray.pt.z)
      self.assertEqual(v.x, ray.dir.x)
      self.assertEqual(v.y, ray.dir.y)
      self.assertEqual(v.z, ray.dir.z)

   def test_ray_equality1(self):
      v1 = Vector(2, 3, 4)
      p1 = Point(2, 3, 4)
      v2 = Vector(2, 3, 4)
      p2 = Point(2, 3, 4)
      self.assertTrue(Ray(p1,v1) == Ray(p2,v2))

   
   def test_ray_equality2(self):
      v1 = Vector(2, 3, 4)
      p1 = Point(3, 4, 5)
      v2 = Vector(2, 3, 4)
      p2 = Point(6, 7, 8)
      self.assertFalse(Ray(p1,v1) == Ray(p2,v2))
      

      

class SphereTests(unittest.TestCase):

   def test_sphere(self):
      
      sph = Sphere(Point(5,4,1),5)
      p=Point(5,4,1)
      self.assertEqual(p.x, sph.center.x)
      self.assertEqual(p.y, sph.center.y)
      self.assertEqual(p.z, sph.center.z)
      self.assertEqual(5, sph.radius)

   def test_sphere_2(self):

      sph = Sphere(Point(1,4,5),3)
      p= Point(1,4,5)
      self.assertEqual(p.x, sph.center.x)
      self.assertEqual(p.y, sph.center.y)
      self.assertEqual(p.z, sph.center.z)
      self.assertEqual(3, sph.radius)

   def test_sphere_equality1(self):
      p1 = Point(2, 3, 4)
      p2 = Point(2, 3, 4)
      self.assertTrue(Sphere(p1,3) == Sphere(p2,3))

   def test_sphere_equality2(self):
      p1 = Point(3, 4, 5)
      p2 = Point(6, 7, 8)
      self.assertFalse(Sphere(p1,3) == Sphere(p2,3))
      



class Scale_Vector_tests(unittest.TestCase):

   def test_vector_scale_1(self):

      v1=Vector(1,1,1)
      v2=Vector(1.5,1.5,1.5)
      self.assertEqual(scale_vector(v1,1.5),v2)

   def test_vector_scale_2(self):
      v1=Vector(2,2,2)
      v2=Vector(4,4,4)
      self.assertEqual(scale_vector(v1,2),v2)

class Dot_vector_tests(unittest.TestCase):

   def test_dot_1(self):

      v1=Vector(1,1,1)
      v2=Vector(2,2,2)
      self.assertEqual(dot_vector(v1,v2),6)
      
   def test_dot_2(self):

      v1=Vector(1,1,1)
      v2=Vector(3,3,3)
      self.assertEqual(dot_vector(v1,v2),9)
            
class Length_vector_tests(unittest.TestCase):

   def test_length_vector1(self):
      v1=Vector(2,2,1)
      self.assertEqual(length_vector(v1),3)

   def test_length_vector2(self):
      v1=Vector(4,3,0)
      self.assertEqual(length_vector(v1),5)

class Normalize_vector_tests(unittest.TestCase):

   def test_normal_1(self):
      v1=Vector(2,2,1)
      self.assertEqual(normalize_vector(v1), Vector(2.0/3,2.0/3,1.0/3))

   def test_normal_2(self):
      v1=Vector(4,3,0)
      self.assertEqual(normalize_vector(v1), Vector(4.0/5,3.0/5,0))
class Difference_point_tests(unittest.TestCase):

   def test_diff_point_1(self):
      p1=Point(2,2,2)
      p2=Point(1,1,1)
      v1=Vector(1,1,1)
      self.assertEqual(difference_point(p1,p2),v1)

   def test_diff_point_2(self):
      p1=Point(3,3,3)
      p2=Point(2,2,2)
      v1=Vector(1,1,1)
      self.assertEqual(difference_point(p1,p2),v1) 

class Difference_vector_tests(unittest.TestCase):

   def test_diff_vector_1(self):
      v1=Vector(2,2,2)
      v2=Vector(1,1,1)
      v3=Vector(1,1,1)
      self.assertEqual(difference_point(v1,v2),v3)

   def test_diff_vector_2(self):
      v1=Vector(3,3,3)
      v2=Point(2,2,2)
      v3=Vector(1,1,1)
      self.assertEqual(difference_point(v1,v2),v3) 


class Translate_point_test(unittest.TestCase):

   def test_translate_point_1(self):
      p1=Point(1,1,1)
      v1=Vector(2,2,2)
      self.assertEqual(translate_point(p1, v1),Vector(3,3,3))
   
   def test_translate_point_2(self):
      p1=Point(2,2,2)
      v1=Vector(3,3,3)
      self.assertEqual(translate_point(p1, v1),Vector(5,5,5))

class Vector_to_from_test(unittest.TestCase):

   def test_vetor_to_from_1(self):
      p1=Point(1,1,1)
      p2=Point(2,2,2)
      self.assertEqual(vector_from_to(p1,p2),Vector(1,1,1))

   def test_vector_to_from_2(self):
      p1=Point(1,1,1)
      p2=Point(3,3,3)
      self.assertEqual(vector_from_to(p1,p2),Vector(2,2,2))
   


                        
if __name__== '__main__':
   unittest.main()
