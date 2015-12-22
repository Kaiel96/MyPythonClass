from sys import argv 
from data import *
from vector_math import *


def main(): 

	try:
		inp = open(argv[1],'r')
	except: 
		print 'Could not open read file'
		return

	try:
		out = open('faded.ppm','w')
	except: 
		print 'Could not write to file'
		return
	
	try: 
		row =  int(argv[2])
		col  = int(argv[3])

	except: 
		print 'nah bro'

	radius = argv[4]
	
	lines = inp.readlines()
	spl = lines[1].split()

	width = int(spl[0])
	hight = int(spl[1])
	out.write(lines[0])
	out.write(lines[1])
	out.write(lines[2])


	pixel = []
	
	x = 1
	y = 1
	
	for pix in lines[3:]:
		
		pixel.append(int(pix))
		dist = math.sqrt((float(x) - float(col))**2 + (float(y) - float(row))**2)
		scale = abs(float(radius) - float(dist))/float(radius)
		if scale < 0.2: 
			scale = 0.2

		if len(pixel) >= 3: 
			r = int(min(pixel[0]*scale,255))
			g = int(min(pixel[1]*scale,255))
			b = int(min(pixel[2]*scale,255))
			out.write(str(r)+' ')
			out.write(str(g)+' ')
			out.write(str(b)+' ')
			pixel = []
			if x == width: 
				x = 1
				y += 1

			else: 
				x += 1
			



if __name__== '__main__':
   main()


