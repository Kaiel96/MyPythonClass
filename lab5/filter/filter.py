def are_positive(nums):
	return [val for val in nums if val>0]

def are_greater_than(nums,n): 
	new=[]
	for val in nums: 
		if val>n:
			new.append(val)
	return new

def are_in_first_quadrent(points):
	new= []
	i=0
	while i< len(points):
		val= points[i]
		i+=1
		if val.x>0 and val.y>0:
                        new.append(val)
	return new


	
