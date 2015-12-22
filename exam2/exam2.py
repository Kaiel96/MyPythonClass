def negatives(nums):
   new = []
   for n in nums: 
   	if n<0: 
   		new.append(n)
   return new

def count_char(s, c):
   count = 0
   for l in s: 
   	if l == c: 
   		count += 1 
   return count
   
def find_max_index(nums):
  i = 0
  for n in range(nums): 
  	if nums[n] > i: 
  		i = nums[n]
  return i 

   
def age_tally(nums):
   children = 0
   adults = 0 
   seniors = 0
   for age in nums: 
   	if age < 18: 
   		children += 1
   	elif age >= 18 and age < 65: 
   		adults += 1
   	else: 
   		seniors += 1
   return (children, adults, seniors)
   
def float_range(min, max):
   new = []
   i = (max - min)/10.0
   for x in range(new):
   	new.append(x+((new[x])*i))
   return new



   

   
