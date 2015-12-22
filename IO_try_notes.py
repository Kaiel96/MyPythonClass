try: 
	x = 'Hey' + 5
	print x

except: 
	print 'something has gone amiss!'

'''File I/O - reading from, writing to files
python casting.py > image.ppm

stuff.py


try: 

	f = open('junk.txt','r')
	out = open('copy.txt','w')

	f = ['Im a file', '13', 'swag']

	for line in f: 
		print line				#prints the file out
		out.write('>' + line + '\n')				#must be a string!!!

except: 
	print 'I'm an albotros'

stuff_2.py 

from sys import *

try:
	f   = open (argv[1],'r')
	out = open(argv[2], 'w')

except:
	print "Could not open file loser, flie you failed was:" + argv[1]

for line in f: 
	print lineout.write('>; + line +'\n'
		)

COMMAND LINE ARGUMENTS





junk.py 

Im a file
13
swag

copy.txt

