def reverse_word(s): 
	rev = []
	for i in range (len(s)): 
		rev.append(s[len(s)-1-i])
	return ''.join(rev)

def find_repeat(nums): 
	for i in range(len(nums-1)-1): 
		if nums[i] == nums[i+1]: 
			return i
	return None