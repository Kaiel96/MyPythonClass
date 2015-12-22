from sys import argv 

def sum_columns(f, c): 
	s = 0
	
	for row in f: 
		spl = row.split()
		if c >= len(spl): 
			print 'Out of range'
		else: 
			try: 
				s += int(spl[c])
				
			except: 
				print 'not a number ' 
	return s 


def main(): 
	f = open(argv[1], 'r')

	try: 
		c = int(argv[2])
	except: 
		print 'Give a better number'
	
	if c < 0: 
		print 'Negatives not allowed'
		return

	print sum_columns(f, c)
	f.close()

if __name__ == '__main__': 
	main()