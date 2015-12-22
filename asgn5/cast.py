from data import *
from collisions import *
import math

def cast_ray(ray, sphere_list, color, light):

	inter = find_intersection_points(sphere_list,ray)

	
	if inter == []:
		return Color(1,1,1)

	min_tuple = inter[0]
	
	for tuples in inter: 
		if distance(tuples[1],ray.pt) < distance(min_tuple[1],ray.pt):
			min_tuple = tuples
	
	r = min_tuple[0].color.r*min_tuple[0].finish.ambiant*color.r
	b = min_tuple[0].color.b*min_tuple[0].finish.ambiant*color.b
	g = min_tuple[0].color.g*min_tuple[0].finish.ambiant*color.g
	
	
	N             = sphere_normal_at_point(min_tuple[0], min_tuple[1])
	pe            = translate_point(min_tuple[1],scale_vector(N,.01))
	L_dir         = normalize_vector(vector_from_to(pe,light.pt))
	
	
	L_dot_N       = dot_vector(N,L_dir)
	reflection    = difference_vector(L_dir,scale_vector(N,2*L_dot_N))
	inter_spheres = find_intersection_points(sphere_list, Ray(pe,L_dir))
	V_dir         = normalize_vector(ray.dir)
	intensity     = dot_vector(reflection,V_dir)

	if intensity > 0: 

		r += light.color.r*min_tuple[0].finish.specular*intensity**(1.0/min_tuple[0].finish.roughness)
		b += light.color.b*min_tuple[0].finish.specular*intensity**(1.0/min_tuple[0].finish.roughness)
		g += light.color.g*min_tuple[0].finish.specular*intensity**(1.0/min_tuple[0].finish.roughness)
		
	if L_dot_N > 0 and inter_spheres == []: 
		r += min_tuple[0].color.r*light.color.r*L_dot_N*min_tuple[0].finish.diffuse
		b += min_tuple[0].color.b*light.color.b*L_dot_N*min_tuple[0].finish.diffuse
		g += min_tuple[0].color.g*light.color.g*L_dot_N*min_tuple[0].finish.diffuse
	
	return Color(r, b, g)

def distance(point1,point2): 
	return math.sqrt((point2.x-point1.x)**2 + (point2.y - point1.y)**2 + (point2.z - point1.z)**2)

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light, file):
		
	incr_x =(max_x-min_x)/float(width)	
	incr_y =(max_y-min_y)/float(height)
	#file.write('P3')
	#file.write (str(width) + ', ' + str(height))
	#file.write('255')

	for iy in range(height):
		act_y = max_y - iy*incr_y
		for ix in range (width):
			act_x = min_x + ix*incr_x
			ray = Ray(eye_point,vector_from_to(eye_point,Point(act_x,act_y,0)))
			
			c = cast_ray(ray, sphere_list,color,light)
			file.write (str(int(min(c.r*255,255))) + ', ' + str(int (min(c.b*255,255))) + ', ' + str (int(min(c.g*255,255))) + '\n')



		



