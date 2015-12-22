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

		except:

			if x == 0:
				print 'bad argument for x, so use default x: Point(' + str(0) + ',' + \
					str(argv[i+2]) + ',' + str(argv[i+3]) + ')'
			elif y == 0:
				print 'bad argument for y, so use default y: Point(' + str(argv[i+1]) + ',' + \
					str(0) + ',' + str(argv[i+3]) + ')'
			elif z == -14: 
				print 'bad argument for y, so use default z: Point(' + str(argv[i+1]) + ',' + \
					str(argv[i+2]) + ',' + str(-14) + ')'
			else: 
				print 'missing argument, so use default eye: Point(' + str(argv[i+1]) + ',' + \
					str(argv[i+2]) + ',' + str(argv[i+3]) + ')'

	
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

			if min_x == -10:
				print 'bad argument , so use default min_x: min_x = ' + str(-10) + ',' + \
					str(argv[i+2]) + ',' + str(argv[i+3]) + str(argv[i+4]) + str(argv[i+5]) + str(argv[i+6])''
			elif max_x == 10:
				print 'bad argument , so use default max_x: Point(' + str(argv[i+1]) + ',' + \
					str(0) + ',' + str(argv[i+3]) + ')'
			elif min_y == -7.5:
				print 'bad argument , so use default min_y: Point(' + str(argv[i+1]) + ',' + \
					str(default_lt_pt.y) + ',' + str(argv[i+3]) + ')'
			elif max_y == 7.5: 
				print 'bad argument , so use default max_y: Point(' + str(default_lt_pt.x) + ',' + ')'
			elif width == 512: 
				print 'bad argument , so use default eye: Point(' ')'
			elif height == 382:
				print 'bad argument , so use default eye: Point(' ')'
			else: 
				print 'missing argument for view, so use default view: Point(' + str(0) + ',' + \
					str(argv[i+2]) + ',' + str(argv[i+3]) + ')'
	
	if "-light" in argv:
		i = argv.index("-light")
		
		try: 

	  		x_l = float_default(argv[i+1],-100)
	  		y_l = float_default(argv[i+2],100)
	  		z_l = float_default(argv[i+3],-100) 
	  		r = float_default(argv[i+4], 1.5)
	  		b = float_default(argv[i+5], 1.5)
	  		g = float_default(argv[i+6], 1.5)

		except:

			if x_l == -100:
				print 'bad argument for x, so use default x: Point(' + str(-100) + ',' + \
					str(argv[i+1]) + ',' + str(argv[i+3]) + ')' + 'Color(' + str(argv[i+4]) + ',' + \
					str(argv[i+5]) + ',' + str(argv[i+6]) + ')'
			elif y_l  == 100:
				print 'bad argument for y, so use default y: Point(' + str(argv[i+1]) + ',' + \
					str(100) + ',' + str(argv[i+3]) + ')' + 'Color(' + str(argv[i+4]) + ',' + \
					str(argv[i+5]) + ',' + str(argv[i+6]) + ')'
			elif z_l == -100:
				print 'bad argument for z, so use default z: Point(' + str(argv[i+1]) + ',' + \
					str(argv[i+2]) + ',' + str(-100) + ')' + 'Color(' + str(argv[i+4]) + ',' + \
					str(argv[i+5]) + ',' + str(argv[i+6]) + ')'
			elif r == 1.5: 
				print 'bad argument for r, so use default r: Point(' + str(argv[i+1]) + ',' + \
					str(argv[i+2]) + ',' + str(argv[i+3]) + ')' + 'Color(' + str(argv[i+4]) + ',' + \
					str(1.5) + ',' + str(argv[i+6]) + ')'
			elif b == 1.5: 
				print 'bad argument b, so use default b: Point(' + str(argv[i+1]) + ',' + \
					str(argv[i+2]) + ',' + str(argv[i+3]) + ')' + 'Color(' + str(argv[i+4]) + ',' + \
					str(1.5) + ',' + str(argv[i+6]) + ')'
			elif g == 1.5:
				print 'bad argument g, so use default g: Point(' + str(argv[i+1]) + ',' + \
					str(argv[i+2]) + ',' + str(argv[i+3]) + ')' + 'Color(' + str(argv[i+4]) + ',' + \
					str(argv[i+5]) + ',' + str(1.5) + ')'
			else: 
				print 'missing argument for light, so use default light: Point(' + str(argv[i+1]) + ',' + \
					str(argv[i+2]) + ',' + str(argv[i+3]) + ')' + 'Color(' + str(argv[i+4]) + ',' + \
					str(argv[i+5]) + ',' + str(argv[i+6]) + ')'


	if "-amb" in argv:
			i = argv.index("-eye")
			
			try: 

			  	r_amb = float_default(argv[i+1], 1.0)
		  		b_amb = float_default(argv[i+2], 1.0)
		  		g_amb = float_default(argv[i+3], 1.0)

		  	except: 
		  		if r_amb == 1.0: 
					print 'bad argument for r, so use default r: Color(' + str(1.0) + ',' + \
						str(argv[i+2]) + ',' + str(argv[i+3]) + ')'
				elif b_amb == 1.0: 
					print 'bad argument b, so use default b: Color(' + str(argv[i+1]) + ',' + \
						str(1.0) + ',' + str(argv[i+3]) + ')'
				elif g_amb == 1.0:
					print 'bad argument g, so use default g: Color(' + str(argv[i+1]) + ',' + \
						str(argv[i+2]) + ',' + str(1.0) + ')'
				else: 
					print 'missing argument for ambiant, so use default ambiant: Color(' + str(argv[i+1]) + ',' + \
						str(argv[i+2]) + ',' + str(argv[i+3]) + ')'
					
	ep = Point(x, y, z)	
	sl = [Sphere(Point(1.0, 1.0,  0.0), 2.0, Color(0.0, 0.0, 1.0), Finish(0.2, 0.4, 0.5, 0.05)), Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1.0, 0.0, 0.0), Finish(0.4, 0.4, 0.5, 0.05))]	
	
	f = open('image.ppm','w')

	cast_all_rays(min_x, max_x, min_y, max_y, width, height, ep, sl, Color(r_amb, b_amb, g_amb), Light(Point(x_l, y_l, z_l), Color(r, b, g)) , f)

	f.close()
		

