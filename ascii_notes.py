
print ord('a') #97
letter = 'a'
print ord(letter) #97

print chr(122) # z

s = 'hello'

func(s)

s.islower() #calls function is lower on string s
	#return True if all alphabetical characters in s are lowercase
s.isupper() #if all letters are uppercase then good

s.isalpha() #true if all characters are alphabetical

def char_upper(c): 
	if c.islower(): 
		u_ord = ord(c) - 32
		return chr(u_ord)
	return c 

s = 'hello'
list = c for c in s #['h', 'e', 'l', 'l', 'o']
list[1] = u

s1 = ''.join(list)

print s1

def str_upper(s): 
	res = [c for c in s]
	for c in res: 
		c = char_upper(c)
	return ''.join(res)
###inefficient, extra unneccisary for loop

def str_upper(s): 
	res = [char_upper(c) for c in s]
	return ''.join(res)

def str_upper(s): 
	res = []
	for c in s: 
		res.append(char_upper(c))
	return ''join(res)

def str_upper(s): 
	result = ''
	for c in s: 
		result = result + char_upper(c)
	return result



