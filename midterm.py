
def avoids(string,forbidden):
	for c in string: 
		if l in forbidden:
			return False
		return True

def guess_a_number(minm,maxm):
	random = randint(minm,maxm)
	num = int(raw_input())

def shift_digits(digits):
	s = []
	for n in digits: 
		if c >= '0' and c < '9': 
			chr(ord(c)+1)
		elif c == '9': 
			c = '0'
		s.append(c)
	return ''.join(s)