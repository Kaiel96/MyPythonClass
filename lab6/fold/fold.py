from point import * 

def sum(nums):
	s=0
	for x in nums:
		s += x
	return s

def index_of_smallest(nums):
	if len(nums) == 0:
		return -1
	smallest = 0
	for current in range(1, len(nums)):
		if nums[current] < nums[smallest]:
			smallest = current
	return smallest

def nearest_origin(nums):
	if len(nums) == 0:
		return -1
	smallest = 0
	for i in range(1,len(nums)): 
		if nums[i].x**2 +nums[i].y**2 <  nums[smallest].x **2 +nums[smallest].y**2: 
			smallest = i
	return smallest


