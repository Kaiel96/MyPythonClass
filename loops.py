#While loops: 
x=0
while x <10:
	print x
	print 'Hello people'
	x = x+1 
x=10
while x>=0:
	x = x-1
	print x
	print 'america'

def blast_off(blast_time):
	while blast_time > 0:
		print blast_time
		blast_time= blast_time-1
	if blast_time == 0:
		print 'Blast Off'

def say_you_are_a_polar_bear():
	answer = 'y' or 'yes'
	while answer == 'n' or 'no':
		print 'You are a polar bear!'
		print 'Do you understand me?:',
		answer = raw_input()
	print 'great...'
		pass
