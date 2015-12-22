def is_lower_101(c):
	if ord(c)>96 and ord(c)<122: 
		return True
	return False

def char_rot_13(c): 
	if c.isalpha:
		if ord(c)>ord('@') and ord(c)<ord('N'): 
			return chr(ord(c)+13)

		elif ord(c)>ord('M') and ord(c)<ord('['):
			return chr(ord(c)-13)
		
		elif ord(c)>ord('`') and ord(c)<ord('n'): 
			return chr(ord(c)+13)

		else: #ord(c)>ord('m') and ord(c)<ord('{'):
			return chr(ord(c)-13)
	return c 




