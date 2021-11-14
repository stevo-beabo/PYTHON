## Video 0 OOP in Python for Beginners (https://www.youtube.com/watch?v=JeznW_7DlB0)

# Creates a class as a blueprint for any object of type dog
class Dog:

	def __init__(self, name, age): # The initial function that instantiates the object and expected attributes when it's called. Self refers to the class itself. This one has a parameter "name"
		self.name = name # Creates an attribute for the parameter "name"
		self.age = age

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def set_age(self, age):
		self.age = age
		print(age)

	def bark(self): # A function that holds an operation that can be performed by the "Dog" class
		print("bark") # The actual operation

	def add_one(self, numb): # A function that expects a parameter (numb)" to be passed to it when it's called
		return numb + 1 

mydog = Dog("Tim", 34) # Assigns a variable to an instance of the class "Dog" and passes a value for "name" and "age"
print(mydog.get_age())
mydog.set_age(23) # Calles the "set_age" function of the class "Dog" to change the "age" attribute from "34" to "23"


mydog.bark() # Calls the specific operation "bark" from the class "Dog" throught the "d" instance
print(mydog.add_one(5)) # Calles the "add_one" operation from the class "Dog" and passes "5" to the "numb" parameter