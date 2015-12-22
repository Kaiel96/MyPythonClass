
def coint_char(c,string): 
	count = 0
	for l in string: 
		if l == c: 
			count += 1
	return count

def student_print(student_list,min_gpa): 
	for s in student_list: 
		if s.gpa > min_gpa: 
			print s.name

def need_affirmation(): 
	answer = False
	while answer == False: 
		print "Am I awesome?,"
		if raw_input() == "Yes": 
			answer = True

def food_drive(): 
	cans = 0
	people = 0
	while cans<100: 
		print 'How many cans do we have?,'
		cans += int(raw_input())
		people += 1
	return (people,cans)

def smallest_tri(tri_list): 
	i = 1
	area = tri_area(tri_list[0])
	triangle = tri_list[0]

	while i < len(tri_list): 
		if tri_area(tri_list[i]) > area: 
			tri_area(tri_list[i]) = area
			tri_list[i] = triangle
	return (area, triangle)



