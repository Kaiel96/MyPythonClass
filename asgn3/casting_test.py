import unittest
from collisions import *
from cast import *
from data import *



class TestCases (unittest.TestCase):
	
	def test_cast_ray_1(self):
		spheres=[Sphere(Point(0,0,0),1),Sphere(Point(4,0,0),1)]
		ray=Ray(Point (-3,0,0),Vector(4,0,0))
		find_int = find_intersection_points(spheres,ray)
		self.assertTrue(cast_ray(ray,spheres))
	
	def test_cast_ray_2(self):
		spheres = [Sphere(Point(-2,0,0),2),Sphere(Point(2,0,0),1)]
		ray = Ray(Point(-5,0,0),Vector(4,0,0))
		find_int = find_intersection_points(ray,spheres)

	def test_cast_cast_all_1(self):
		spheres=[Sphere(Point(1.0,1.0,0),2),Sphere(Point(0.5,1.5,-3.0),0.5)]
		cast_all_rays(-10,10,-7.5,7.5,512,384,Point(0,0,-10),spheres)


if __name__ == '__main__':
   unittest.main()


