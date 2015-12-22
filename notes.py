# List Comprehensions

#1) Map Patterns

nums = [1,5,3,10]
doubles = [2*x for x in nums]

print doubles


class Student:
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa

students=[Student('joe',2.91), Student('Jan',3.13)]

curved=[Student(s.name,s.gpa+0.2) for s in students]

#2) Filter Patterns

nums2 = [1,2,5,7,8,-10,100,131]
evens = [x for x in nums2 if x%2==0]

honors = [s for s in students if s.gpa>3.0]
print honors[0].gpa #3.13

honors[0].gpa = 4.0

print (students[1].gpa)

honors = [Student(s.name,s.gpa) for s in students if s.gpa>3.0]


