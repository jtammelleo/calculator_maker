#Multiply
def multiply(a,b):
	return a * b
 
#Divide
def divide(a,b):
	return a / b

#Add
def add(a,b):
	return a + b

#Subtract
def subtract(a,b):
	return a - b

#Square
def square(a):
	return a * a

#Cube
def cube(a):
	return a * a * a

#Square_n_times
def sqn(a,b):
	return a**b

print("I'm going to use the calculator functions to multiply 5 and 6")
m = multiply(5,6)
print(m)

print("I'm going to use the calculator functions to divide 5 and 6")
d = divide(5,6)
print(d)

print("I'm going to use the calculator functions to add 5 and 6")
z = add(5,6)
print(z)

print("I'm going to use the calculator functions to subtract 5 and 6")
s = subtract(5,6)
print(s)

print("I'm going to use the calculator functions to square 5")
q = square(5)
print(q)

print("I'm going to use the calculator functions to cube 5")
c = cube(5)
print(c)

print("I'm going to use the calculator functions to exponent 5, 6 times")
e = sqn(5,6)
print(e)