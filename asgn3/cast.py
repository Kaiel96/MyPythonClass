from collisions import *

def cast_ray(ray, sphere_list):
	if find_intersetion_points(sphere_list,ray) != []:
		return True
	return False

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):

	incr_x =(max_x-min_x)/width	
	incr_y =(max_y-min_y)/height
	print P3 
	print width, height
	print 255

	for iy in range(height):
		act_y=iy*incr_y+min_y
		for ix in range (width):
			act_x=ix*incr_x+min_x
			print '(' + str(act_x) + str(act_y) + ')', 
		print ''
		ray = vector_from_to(eye_point,Point(act_x,act_y,0))
		if cast_ray(ray,sphere_list):
			print 0 0 0
		else:
			print 255 255 255



		



