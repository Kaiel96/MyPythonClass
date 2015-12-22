import unittest
from data import *
import math
from vector_math import*
from collisions import*

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
      self.assertEqual(378.5, v.x)
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

      r = Ray(Point(2,3,1), Vector(3,1,2))
      p = Point(2,3,1)
      v = Vector(3,1,2)
      self.assertEqual(p.x, r.pt.x)
      self.assertEqual(p.y, r.pt.y)
      self.assertEqual(p.z, r.pt.z)
      self.assertEqual(v.x, r.dir.x)
      self.assertEqual(v.y, r.dir.y)
      self.assertEqual(v.z, r.dir.z)

   def test_ray_2(self):   
      
      r = Ray(Point(4,5,6),Vector(7,8,9))
      p = Point(4,5,6)
      v = Vector(7,8,9)
      self.assertEqual(p.x, r.pt.x)
      self.assertEqual(p.y, r.pt.y)
      self.assertEqual(p.z, r.pt.z)
      self.assertEqual(v.x, r.dir.x)
      self.assertEqual(v.y, r.dir.y)
      self.assertEqual(v.z, r.dir.z)

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
      
      s = Sphere(Point(5,4,1),5,Color(1,0,0),Finish(1.0,.4,.5,.05))
      p = Point(5,4,1)
      c = Color(1,0,0)
      f = Finish(1.0,.4,.5,.05)
      self.assertEqual(p.x, s.center.x)
      self.assertEqual(p.y, s.center.y)
      self.assertEqual(p.z, s.center.z)
      self.assertEqual(5, s.radius)
      self.assertEqual(c.r, s.color.r)
      self.assertEqual(c.b, s.color.b)
      self.assertEqual(c.g, s.color.g)
      self.assertEqual(f.ambiant, s.finish.ambiant)
      self.assertEqual(f.diffuse, s.finish.diffuse)
      self.assertEqual(f.specular, s.finish.specular)
      self.assertEqual(f.roughness, f.roughness)


   def test_sphere_2(self):

      s = Sphere(Point(1,4,5),3,Color(1,0,0),Finish(1.0,.4,.5,.05))
      p = Point(1,4,5)
      c = Color(1,0,0)
      f = Finish(1.0,.4,.5,.05)
      self.assertEqual(p.x, s.center.x)
      self.assertEqual(p.y, s.center.y)
      self.assertEqual(p.z, s.center.z)
      self.assertEqual(3, s.radius)
      self.assertEqual(c.r, s.color.r)
      self.assertEqual(c.b, s.color.b)
      self.assertEqual(c.g, s.color.g)
      self.assertEqual(f.ambiant, s.finish.ambiant)
      self.assertEqual(f.diffuse, s.finish.diffuse)
      self.assertEqual(f.specular, s.finish.specular)
      self.assertEqual(f.roughness, f.roughness)

   def test_sphere_equality1(self):
      p1 = Point(2, 3, 4)
      p2 = Point(2, 3, 4)
      c1 = Color(1, 0, 0)
      c2 = Color(1, 0, 0)
      f1 = Finish(1.0,.4,.5,.05)
      f2 = Finish(1.0,.4,.5,.05)
      self.assertEqual(Sphere(p1,3,c1,f1), Sphere(p2,3,c2,f2))

   def test_sphere_equality2(self):
      p1 = Point(3, 4, 5)
      p2 = Point(3, 4, 5)
      c1 = Color(0, 0, 1)
      c2 = Color(0, 0, 1)
      f1 = Finish(1.0,.3,.5,.01)
      f2 = Finish(1.0,.3,.5,.01)
      self.assertEqual(Sphere(p1,3,c1,f1), Sphere(p2,3,c2,f2))
      



class Scale_Vector_tests(unittest.TestCase):

   def test_vector_scale_1(self):

      v1 = Vector(1,1,1)
      v2 = Vector(1.5,1.5,1.5)
      self.assertEqual(scale_vector(v1,1.5),v2)

   def test_vector_scale_2(self):
      v1 = Vector(2,2,2)
      v2 = Vector(4,4,4)
      self.assertEqual(scale_vector(v1,2),v2)

class Dot_vector_tests(unittest.TestCase):

   def test_dot_1(self):

      v1 = Vector(1,1,1)
      v2 = Vector(2,2,2)
      self.assertEqual(dot_vector(v1,v2),6)
      
   def test_dot_2(self):

      v1 = Vector(1,1,1)
      v2 = Vector(3,3,3)
      self.assertEqual(dot_vector(v1,v2),9)
            
class Length_vector_tests(unittest.TestCase):

   def test_length_vector1(self):
      v = Vector(2,2,1)
      self.assertEqual(length_vector(v),3)

   def test_length_vector2(self):
      v = Vector(4,3,0)
      self.assertEqual(length_vector(v),5)

class Normalize_vector_tests(unittest.TestCase):

   def test_normal_1(self):
      v = Vector(2,2,1)
      self.assertEqual(normalize_vector(v), Vector(2.0/3,2.0/3,1.0/3))

   def test_normal_2(self):
      v = Vector(4,3,0)
      self.assertEqual(normalize_vector(v), Vector(4.0/5,3.0/5,0))

class Difference_point_tests(unittest.TestCase):

   def test_diff_point_1(self):
      p1 = Point(2,2,2)
      p2 = Point(1,1,1)
      v  = Vector(1,1,1)
      self.assertEqual(difference_point(p1,p2),v)

   def test_diff_point_2(self):
      p1 = Point(3,3,3)
      p2 = Point(2,2,2)
      v  = Vector(1,1,1)
      self.assertEqual(difference_point(p1,p2),v) 

class Difference_vector_tests(unittest.TestCase):

   def test_diff_vector_1(self):
      v1 = Vector(2,2,2)
      v2 = Vector(1,1,1)
      v3 = Vector(1,1,1)
      self.assertEqual(difference_point(v1,v2),v3)

   def test_diff_vector_2(self):
      v1 = Vector(3,3,3)
      v2 = Point(2,2,2)
      v3 = Vector(1,1,1)
      self.assertEqual(difference_point(v1,v2),v3) 


class Translate_point_test(unittest.TestCase):

   def test_translate_point_1(self):
      p = Point(1,1,1)
      v = Vector(2,2,2)
      self.assertEqual(translate_point(p, v),Vector(3,3,3))
   
   def test_translate_point_2(self):
      p = Point(2,2,2)
      v = Vector(3,3,3)
      self.assertEqual(translate_point(p, v),Vector(5,5,5))

class Vector_to_from_test(unittest.TestCase):

   def test_vetor_to_from_1(self):
      p1 = Point(1,1,1)
      p2 = Point(2,2,2)
      self.assertEqual(vector_from_to(p1,p2),Vector(1,1,1))

   def test_vector_to_from_2(self):
      p1 = Point(1,1,1)
      p2 = Point(3,3,3)
      self.assertEqual(vector_from_to(p1,p2),Vector(2,2,2))
   
class Test_Collisions(unittest.TestCase):

#This will test the case where the sphere is hit twice by the ray (both t positive)

   def test_coll_1(self):
      r = Ray(Point(-2,0,0),Vector(0.5,0,0))
      #Ray r will intersect with Sphere s
      s = Sphere(Point(0,0,0),1, Color(1,0,0),Finish(1.0,.4,.5,.05))
      actual = sphere_intersection_point(r,s)
      self.assertEqual(actual, Point(-1,0,0)) #Sphere hits at point(0,-1,0) first

#This will test where sphere is hit and the ray is Tangent to the sphere(discrim=0 one t value)
      
   def test_coll_2(self):
      r = Ray(Point(-3,1,0),Vector(4,0,0))
      s = Sphere(Point(0,0,0),1, Color(1,0,0),Finish(1.0,.4,.5,.05))
      #the ray will not intersect with Sphere s
      actual = sphere_intersection_point(r,s)
      self.assertEqual(actual, Point(0,1,0)) #intersects at tangent point (0,1,0)

# This is where the sphere and the vector do not intersect whatsoever (

   def test_coll_3(self):
      r = Ray(Point(1,4,0),Vector(4,0,0))
      s = Sphere(Point(0,0,0),1,Color(1,0,0),Finish(1.0,.4,.5,.05))
      self.assertEqual(sphere_intersection_point(r,s), None)

#This is where the ray starts at the edge if the sphere and moves away(both t<0)

   def test_coll_4(self):
      r = Ray(Point(1,0,0),Vector(4,0,0))
      s = Sphere(Point(0,0,0),1, Color(1,0,0),Finish(1.0,.4,.5,.05))
      self.assertEqual(sphere_intersection_point(r,s), None)

#This is where the ray starts in the sphere and moves outwards(one t pos one t neg)

   def test_coll_5(self):
      r = Ray(Point(0,0,0),Vector(4,0,0))
      s = Sphere(Point(0,0,0),5,Color(1,0,0),Finish(1.0,.4,.5,.05))
      self.assertEqual(sphere_intersection_point(r,s), Point(5,0,0))
      

#This will test the case where the sphere is hit twice by the ray (both t positive)

   def test_coll_non_axis_1(self):
      r = Ray(Point(-6,3,0),Vector(1,0,0))
      #Ray r will intersect with Sphere s
      s = Sphere(Point(-3,3,0),2,Color(1,0,0),Finish(1.0,.4,.5,.05))
      actual = sphere_intersection_point(r,s)
      self.assertEqual(actual, Point(-5,3,0)) #Sphere hits at point (-5,3,0) first

#This will test where sphere is hit and the ray is Tangent to the sphere(discrim=0 one t value)
      
   def test_coll_non_axis_2(self):
      r = Ray(Point(-6,5,0),Vector(4,0,0))
      s = Sphere(Point(-3,3,0),2,Color(1,0,0),Finish(1.0,.4,.5,.05))
      actual = sphere_intersection_point(r,s)
      #the ray will not intersect with Sphere s
      self.assertEqual(actual, Point(-3,5,0)) #intersects at tangent point (-3,5,0)

# This is where the sphere and the vector do not intersect whatsoever (

   def test_coll_non_axis_3(self):
      r = Ray(Point(-8,1,0),Vector(1,4,0))
      s = Sphere(Point(-3,3,0),2,Color(1,0,0),Finish(1.0,.4,.5,.05))
      self.assertEqual(sphere_intersection_point(r,s), None)

#This is where the ray starts at the edge if the sphere and moves away(both t<0)

   def test_coll_non_axis_4(self):
      r = Ray(Point(-1,3,0),Vector(4,0,0))
      s = Sphere(Point(-3,3,0),2,Color(1,0,0),Finish(1.0,.4,.5,.05))
      self.assertEqual(sphere_intersection_point(r,s), None)

#This is where the ray starts in the sphere and moves outwards(one t pos one t neg)

   def test_coll_non_axis_5(self):
      r = Ray(Point(-3,3,0),Vector(4,0,0))
      s = Sphere(Point(-3,3,0),2,Color(1,0,0),Finish(1.0,.4,.5,.05))
      actual=sphere_intersection_point(r,s)
      self.assertEqual(actual, Point(-1,3,0))

class Test_intersection_points(unittest.TestCase):

   def test_int_2_pts_1(self):
      s1 = Sphere(Point(-2,0,0),1, Color(1,0,0),Finish(1.0,.4,.5,.05))
      s2 = Sphere(Point(2,0,0),1, Color(1,0,0),Finish(1.0,.4,.5,.05))
      spheres = [s1, s2]
      expected = [(s1,Point(-3,0,0)),(s2,Point(1,0,0))] # 2 spheres intersected at 2 points (-3,0,0) and (1,0,0) with a ray
      r = Ray(Point(-5,0,0),Vector(5,0,0))
      self.assertEqual(find_intersection_points(spheres,r), expected)

   def test_int_1_pt_1(self):
      s1 = Sphere(Point(-2,0,0),1, Color(1,0,0),Finish(1.0,.4,.5,.05))
      s2 = Sphere(Point(2,0,0),1, Color(1,0,0),Finish(1.0,.4,.5,.05))
      spheres = [s1, s2]
      expected = [(s2,Point(1,0,0))] # 1 sphere intersected at 1 points with a ray
      r=Ray(Point(0,0,0),Vector(5,0,0))
      self.assertEqual(find_intersection_points(spheres,r), expected)

   def test_int_no_point(self):
      s1 = Sphere(Point(-2,0,0),1,Color(1,0,0),Finish(1.0,.4,.5,.05))
      s2 = Sphere(Point(2,0,0),1,Color(1,0,0),Finish(1.0,.4,.5,.05))
      spheres  = [s1, s2]
      expected = [] # 0 spheres are hit by the ray
      r=Ray(Point(5,0,0),Vector(5,0,0))
      self.assertEqual(find_intersection_points(spheres,r), expected)

   def test_int_2_tangents(self):
      s1 = Sphere(Point(-2,0,0),1,Color(1,0,0),Finish(1.0,.4,.5,.05))
      s2 = Sphere(Point(2,0,0),1,Color(1,0,0),Finish(1.0,.4,.5,.05))
      spheres  = [s1, s2]
      expected = [(s1,Point(-2,1,0)),(s2,Point(2,1,0))] # 2 spheres are hit by the ray at 2 points with tangents
      r  = Ray(Point(-3,1,0),Vector(5,0,0))
      actual   = find_intersection_points(spheres,r)
      self.assertEqual(find_intersection_points(spheres,r), expected)
      
   
class Test_Sphere_normal_at_point(unittest.TestCase):

   def test_sphere_normal_1(self):
      s = Sphere(Point(0,0,0),5,Color(1,0,0),Finish(1.0,.4,.5,.05))
      p = Point(5,0,0)
      v = vector_from_to(s.center,p)#create the vector from the center to the edge of the sphere 
      self.assertEqual(sphere_normal_at_point(s,p),normalize_vector(v))

   
   def test_sphere_normal_2(self):
      s = Sphere(Point(3,4,0),2,Color(1,0,0),Finish(1.0,.4,.5,.05))
      p = Point(0,6,0)
      v = vector_from_to(s.center,p)#create the vector from the center to the edge of the sphere 
      self.assertEqual(sphere_normal_at_point(s,p),normalize_vector(v))

if __name__== '__main__':
   unittest.main()
