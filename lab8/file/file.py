from sys import argv
try:
	f = open(argv[1],'r')
except: 
	print 'OMG u noob did not operate lullll'
	exit()

f = open(argv[1], 'r')
i = 1
for line in f: 
	i += 1
	try: 
		l = line.split()
		x = float(l[0]) + float(l[1])
		print x

	except: 
		print 'error in line' + str(i) 
	
