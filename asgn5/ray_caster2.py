from cast import *
from data import *
from sys import argv

def main():

	for x in argv:	
		width = 512
		height = 384

		print 'P3'
		print width, height
		print 255
		f = open('image.ppm','w')

		ep = Point(0, 0, -14)
		sl = [Sphere(Point(1.0, 1.0,  0.0), 2.0, Color(0.0, 0.0, 1.0), Finish(0.2, 0.4, 0.5, 0.05)), Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1.0, 0.0, 0.0), Finish(0.4, 0.4, 0.5, 0.05))]
		cast_all_rays(-10, 10, -7.5, 7.5, width, height, ep, sl, Color(1.0, 1.0, 1.0), Light(Point(-100, 100, -100), Color(1.5, 1.5, 1.5)),f)

		f.close()

		f = open('image.ppm','r')
		lines = f.readlines()
		i = 0
	
		for l in lines: 
			try:
				i += 1
				spl = l.split(" ")
				s = Sphere(Point(float(spl[0]), float(spl[1]), float(spl[2])), float(spl[3]), \
		 		Color(float(spl[4]), float(spl[5]), float(spl[6])), Finish(float(spl[7]), float(spl[8]),\
		  		float(spl[9]), float(spl[10])))
		  		
		  		
			except: 
				print 'malformed sphere on line ' + str(i) + '... skipping'

		'''try: 
		  		if "-eye" in argv:
		  			i = argv.index("-eye")
		  			argv[i+1]

		  		elif "-amb" in argv:
		  			i = argv.index("-amb") 
		  			argv[i+1]

		  		elif "-view" in argv: 
		  			i = argv.index("-view")
		  			argv[i + 1]
		  			argv[i + 2]
		  			argv[i + 3]
		  			argv[i + 4]
		  			argv[i + 5]
		  			argv[i + 6]

		  		elif "-light" in argv: 
		  			i = argv.index("-light")
		  			argv[i+1]
		except: '''



		



if __name__ == '__main__': 
	main()



