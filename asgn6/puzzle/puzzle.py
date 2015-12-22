from sys import argv

if len(argv) < 1:
	print 'No arguement provided... ending program'

def main(): 
	try:
		inp = open(argv[1],'r')
	except: 
		print 'Could not open file'
		return

	try:
		out = open('hidden.ppm','w')
	except: 
		print 'Could not write to file'
		return
	#line = inp.readline()
	lines = inp.readlines()
	out.write(lines[0])
	out.write(lines[1])
	out.write(lines[2])
	
	pixel = []
	
	for pix in lines[3:]:
		pixel.append(int(pix))
		if len(pixel) >= 3: 
			r = min(pixel[0]*10,255)
			g = min(pixel[0]*10,255)
			b = min(pixel[0]*10,255)
			out.write(str(r)+' ')
			out.write(str(g)+' ')
			out.write(str(b)+' ')
			pixel = []
			
				



if __name__ == '__main__': 
	main()
		
		
