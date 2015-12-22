def group_of_3(nums): 
	if len(nums) == 0:
		return []
	extend = [[]]
	for x in nums: 
		if len(extend[-1]) == 3: 
			extend.append([])
		extend[-1].append(x)
	return extend 
