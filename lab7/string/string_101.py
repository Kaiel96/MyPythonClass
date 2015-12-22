from char import *

def str_rot_13(string): 
	result = ''
	for c in string: 
		result += char_rot_13(c)

	return result

def str_translate_101(string,old,new):
	result = ''
	for c in string: 
		if c == old: 
			result += new
		else:
			result += c
	return result


