from cast import *
from data import *
from sys import argv

def float_default(string,default_float_val):

	try: 
		return float(string)

	except: 
		return default_float_val
	


if "-eye" in argv:
	i = argv.index("-eye")
	
	try:
  		x = float_default(argv[i+1],0)
		y = float_default(argv[i+2],0)
		z = float_default(argv[i+3],-14)
		eye_point= Point(x,y,z) 
	
	except: 
		print 'madness!'
else:
	x = 0 
	y = 0
	z = -14
	eye_point= Point(x,y,z) 

if "-view" in argv:
	i = argv.index("-view")
	

	try: 

  		min_x = float_default(argv[i+1],-10)
  		max_x = float_default(argv[i+2],10)
  		min_y = float_default(argv[i+3],-7.5)
  		max_y = float_default(argv[i+4], 7.5)
  		width = float_default(argv[i+5], 512)
  		height = float_default(argv[i+6], 382)

  	except: 
  		print 'no mang'

else:

	min_x = -10
	max_x = 10
	min_y = -7.5
	max_y =  7.5
	width =  512
	height =  382


if "-light" in argv:
	i = argv.index("-light") 

	try: 

  		x = float_default(argv[i+1],-100)
  		y = float_default(argv[i+2],100)
  		z = float_default(argv[i+3],-100) 
  		r = float_default(argv[i+4], 1.5)
  		b = float_default(argv[i+5], 1.5)
  		g = float_default(argv[i+6], 1.5)
  		pt = Point(x,y,z)
		color = Color(r,b,g)
		light = Light(pt,color)

	except:
		print 'naw'

else:
	x = -100
	y = 100
	z = -100
	r = 1.5
	b = 1.5
	g = 1.5
	pt = Point(x,y,z)
	color = Color(r,b,g)
	light = Light(pt,color)


if "-amb" in argv:
		
	i = argv.index("-eye")
	try: 

	  	r = float_default(argv[i+1], 1.0)
  		b = float_default(argv[i+2], 1.0)
  		g = float_default(argv[i+3], 1.0)
  		color = Color(r,b,g)

  	except:
  		print 'murica'
 
else: 
 	r = 1.0
 	b = 1.0
 	g = 1.0
 	color = Color(r,b,g)







