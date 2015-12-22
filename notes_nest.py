#nested loops

for i in range(10):
	for j in range (25):
		print "two fiddy"
	print 'doller bills'
print done

def print_table(max_row, max_col):
	for r in range(max_row):
		for c in range(max_col):
			print '(',r+1,c+1,(r+1)*(c+1),')',
		print ""

#max and mins

nums = [83, 42, 10, 28, 6, 100, 230]

x = find_min(nums)
print x #expect x

def find_min(quant): 
	if quant == []:
		return None
	min_val = quant[0]
	for i in range(1,len(quant)): 
		if quant[i]<min_val:
			min_val = quant[spot]
	return min_val

def find_min_val(quant):
	if len(quant) == 0: 
		return None
	min_val = quant[0]
	for val in quant:
		if val < min_val:
			



