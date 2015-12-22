from sys import *
if len(argv) != 3: 
	print "Lolz, u suk senpai"
	exit()
try:
	f   = open (argv[1],'r')
	out = open(argv[2], 'w')

except:
	print "Could not open file loser, flie you failed was:" + argv[1]

for line in f: 
	print line 
	out.write('>'+ line +'\n')

# python stuff_2.py junk.txt copy387.txt

line = 'this is a very long sentence'
words = line.split()
print words

#['this','is', 'a', 'long', 'sentence']

for line in f: 
	words = line.split()
	for w in words: 
		print w 
		out.write('>' + w + '\n')
