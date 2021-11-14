## Video 4 of Object Oriented Programming with Python (https://www.youtube.com/watch?v=39m3rstTN8w)

# Example of overriding the built-in functions found in Python
class Point():
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		self.coords = (self.x, self.y)

	def move(self, x, y):
		self.x += x
		self.y += y

	def __add__(self, p): # __add_ is the built-in Python "+" function to add integers and return their sum
		return Point(self.x + p.x, self.y + p.y)

	def __sub__(self, p): # __sub_ is the built-in Python "-" function to subtracts integers and return their difference
		return Point(self.x - p.x, self.y - p.y)

	def __mul__(self, p): # __mul_ is the built-in Python "*" function to multiples integers and return their product
		return self.x * p.x + self.y * p.y

#	def __div__(self, p): # # __div_ is the built-in Python "/" function to divides integers. Was not covered in the tutorial
#		return Point(self.x / p.x, self.y / p.y)

	def length(self): # The built-in function __len__ will find the length of characters in a string or integer
		import math # Importing the library "math" to square the results. (aka x to the power of 2)
		return math.sqrt(self.x**2 + self.y**2)

	def __gt__(self, p): # __gt_ is the built-in Python ">" function to compare the value of two integers and returns a Boolean if the first is a greater value
		return self.length() > p.length()

	def __ge__(self, p): # __ge_ is the built-in Python ">=" function to compare the value of two integers and returns a Boolean if the first is a greater or equal value
		return self.length() >= p.length()

	def __lt__(self, p): # __lt_ is the built-in Python "<" function to compare the value of two integers and returns a Boolean if the first is a lesser value
		return self.length() < p.length()

	def __le__(self, p): # __le_ is the built-in Python ">=" function to compare the value of two integers and returns a Boolean if the first is a lesser or equal value
		return self.length() <= p.length()

	def __eq__(self, p): # __eq_ is the built-in Python "==" function to compare the value of two integers and returns a Boolean if the first is of equal value
		return self.x == p.x and self.y == p.y

	def __str__(self): # __str_ is the built-in Python "str" function to translate values into a string data type
		return "(" +str(self.x) + "," + str(self.y) + ")"

# Setting grid point values for the example
p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)

# Using the new overriden methods to get a result of complex variables
p5 = p1 + p2
p6 = p4 - p1
p7 = p2*p3
print(p5, p6, p7)

# Using the new overriden methods to compare the values of the points by their distance from (0,0) on the grid
print(p1 == p2)
print(p1 > p2)
print(p4 <= p3)

