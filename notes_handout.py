nums = [1,2,3,4,7,56,67,89,342,231,234,744,4235,8345]
print (nums)

squares = [value*value for value in nums]
print (squares)
print (squares [4])

square_tuples = [(value,value*value) for value in nums]
print (square_tuples)
print (square_tuples[0])
print (square_tuples[0][0]) #this will give value within the index
print (square_tuples[5][0])#error

def func(x):
    return x**2 - 23.6*x - 100

vals = [funcs(val) for val in nums]
print vals


val_tuples = [(val, func(val)) for val in nums]
print val_tuples



def int_div(x, y):
    return (x/y, x%y)

div_7 = [int_div(value, 7) for value in nums]
print div_7




even_div_7 = [val for val in div_7 if val[1] == 0]

