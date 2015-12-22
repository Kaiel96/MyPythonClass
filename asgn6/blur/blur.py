from sys import argv

def group_of_3(nums):
	if len(nums) == 0:
		return []
	extend = [[]]
	for x in nums:
		if len(extend[-1]) == 3: 
			extend.append([])
		extend[-1].append(x)
	return extend 

def float_default(string,default_float_val):
	
	try: 
		return float(string)

	except: 
		return default_float_val

def pixel_reader(data): 
	pixels = []
	lines = group_of_3(data.split()[4:])
	for i in range(len(lines)):
		r = min(int(lines[i][0]),255)
		g = min(int(lines[i][1]),255)
		b = min(int(lines[i][2]),255)
		p = [r,b,g]
		pixels.append(p)
	return pixels


def blur(pixels,reach,height,width): 
	pixel_squad = []
	for row in range(height): 
		for col in range(width): 
			num = 0
			r = 0
			b = 0
			g = 0 
			for r_count in range(max(int(row) - int(reach), 0), min(int(row) + int(reach), height)):
				for c_count in range(max(int(col) - int(reach), 0), min(int(col) + int(reach), width)):
					r += pixels[r_count * width + c_count][0]
					g += pixels[r_count * width + c_count][1]
					b += pixels[r_count * width + c_count][2]
					num += 1
			r /= num
			g /= num
			b /= num
			p = [r,g,b]
			pixel_squad.append(p)
	return pixel_squad


def file_write(f,pixels,height,width): 
	#print pixels
	for p in pixels:
		f.write(str(p[0])+" "+str(p[1])+" "+str(p[2])+" ")


def main(): 

	try: 
		inp = open(argv[1],'r')
		data = inp.read()
		spl = data.split()
		width = int(spl[1])
		height = int(spl[2])


	except: 
		print "Could not open read file 1"
		return None


	try: 
		out = open('blurred.ppm', 'w')
		out.write(spl[0])
		out.write('\n')
		out.write(spl[1])
		out.write(' ')
		out.write(spl[2])
		out.write('\n')
		out.write(spl[3])
		out.write('\n')

	except:
		print "Could not open write file"
		return None

	try: 
		reach = argv[2]

	except: 
		reach = 4

	try:
		pixels = pixel_reader(data)
	except: 
		print "Could not open read file 2"
		return None

	bluring = blur(pixels, reach, height, width)

	try:
		file_write(out, bluring,height,width)
	except: 
		print "fail bro"
		return None
	
if __name__== '__main__':
	main()

