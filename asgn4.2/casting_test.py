import unittest
from collisions import *
from cast import *
from data import *



class TestCases (unittest.TestCase):
	
	#def test_cast_ray_1(self):
		#spheres=[Sphere(Point(0,0,0),1, Color(0,1,0)),Sphere(Point(4,0,0),1,Color(0,1,0))]
		#ray=Ray(Point (-3,0,0),Vector(4,0,0))
		#self.assertTrue(cast_ray(ray,spheres),True)
	
	#def test_cast_ray_2(self):
		#spheres = [Sphere(Point(-2,0,0),2,Color(0,1,0)),Sphere(Point(2,0,0),1,Color(0,1,0))]
		#ray = Ray(Point(-5,0,0),Vector(4,0,0))
		#self.assertTrue(cast_ray(ray,spheres),True)

	#def test_cast_ray_3(self):
		#spheres = [Sphere(Point(2,0,0),1,Color(0,1,0)),Sphere(Point(-2,0,0),2,Color(0,1,0))]
		#ray = Ray(Point(-5,0,0),Vector(4,0,0))
		#self.assertTrue(cast_ray(ray,spheres),True)
	width = 512
	height = 384
	print 'P3'
	print width, height
	print 255

	def test_cast_cast_all_1(self):
		ep = Point(0, 0, -14)
		sl = [Sphere(Point(1.0, 1.0,  0.0), 2.0, Color(0.0, 0.0, 1.0), Finish(0.2, 0.4, 0.5, 0.05)), 
      	Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1.0, 0.0, 0.0), Finish(0.4, 0.4, 0.5, 0.05))]
      	cast_all_rays(-10, 10, -7.5, 7.5, width, height, ep, sl, Color(1.0, 1.0, 1.0), Light(Point(-100, 100, -100), Color(1.5, 1.5, 1.5)))

if __name__ == '__main__':
   unittest.main()


