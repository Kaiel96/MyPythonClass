from cast import *
from data import *
from sys import argv
from commandline import *

def main():

	try:
		f = open(argv[1],'r')
	except: 
		print 'Could not open file'
		return
	try: 
		m = open('image.ppm','w')
	except:
		print 'Could not open output file'
		return
	
	sph_list = []
	lines = f.readlines()
	i = 0

	for l in lines: 
		i += 1
		spl = l.split(" ")
		try:
			s = Sphere(Point(float(spl[0]), float(spl[1]), float(spl[2])), float(spl[3]), \
	 		Color(float(spl[4]), float(spl[5]), float(spl[6])), Finish(float(spl[7]), float(spl[8]),\
	  		float(spl[9]), float(spl[10])))
	  		sph_list.append(s) 

	  		
		except: 
			print 'malformed sphere on line ' + str(i) + '... skipping'
	
	try: 
		m.write('P3\n')
		m.write(str(width) + ' ' + str(height) + '\n')
		m.write('255\n')
		cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sph_list, color, light, m) 

	except: 
		print 'Could not write properly'

if __name__ == '__main__': 
	main()



