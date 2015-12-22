from math import *

def square_all(nums):
	return [x**2 for x in nums]

def add_n_all(nums,v):
	new= []
	for n in nums:
                new.append(n+v)
	return new

def distance_all(points):
	new = []
	i = 0 
	while i<len(points):
		val=points[i]
		i += 1
		new.append(sqrt(val.x**2+val.y**2))
	return new
	
	


