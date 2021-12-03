## Video 5 of Object Oriented Programming with Python (https://www.youtube.com/watch?v=MpuOuZKWUWw)

class Dog:
	dogs = [] # Class variable, able to be called without making an instance of the class

	def __init__(self, name):
		self.name = name
		self.dogs.append(self) # Appends every dog object into the the list variable "dogs"

	@classmethod # Method Decorator to indicate the special type of method. Class Methods can be called without making an instance of the class
	def num_dogs(cls): # Class Methods use the parameter "cls" instead of "self"
		return len(cls.dogs)

	@staticmethod # Method Decorator to indicate the special type of method. Static Methods do not need the class or an instance of a class to be called. Cannot be refernced inside of the class either.
	def bark(n): # Barks "n" amounts of times
		for _ in range(n):
			print("Bark!")


class Math:
	@staticmethod
	def add(x, x2):
		return x + x2

#tim = Dog("Tim")
#jim = Dog("Jim")

print(Dog.dogs) # Prints out the value of the class variable 
print(Dog.num_dogs()) # Prints out the results of the "num_dogs" method without creating an instance object first
Dog.bark(5) # Use of the Static Method "bark" in the class Dog
print(Math.add(5, 5)) # Using the Static Method "add" in the class Math