## Video 2 of Object Oriented Programming with Python (https://www.youtube.com/watch?v=jQiUOV15IRI)

class Dog(object):
	def __init__(self, name, age): # The method that automatically runs when the class is called. No need to specically call it with "Dog().__initi__"
		self.name = name # "self" refers to the instance of the class when it is running so it can be used independantly by multiple instances of the same class
		self.age = age
		self.li = [1,3,4]

	def speak(self):
		print("Hi I am", self.name, "and I am", self.age, "years old")

	def change_age(self, age):
		self.age = age

	def add_weight(self, weight): # "weight" is being defined outside of "__init__" so can only be set once "add_wieght" has been specifcally called
		self.weight = weight

tim = Dog("Tim", 55) # Builds a constructor of the the class "Dog()" and puts it into a variable. "Tim" & "55" is passed to "Dog) since it is expecting the "name" and "age" attribute
fred = Dog("Fred", 3)

tim.change_age(5) # Uses the "change_age" method under "Dog()" to change the "age" attribute to 5

tim.add_weight(70)
print(tim.weight)
#print(fred.weight) This will not run correct as the attribute "weight" is defined in the "add_weight" method not in "__init__" and "fred.add_weight" has not been set

tim.speak() # Runs the "speak" method under "Dog()" for instance "tim"
fred.speak() # Runs the "speak" method under "Dog()" for instance "fred"

print(tim.age) # Finds the value of "self.age" without using a method
print(tim.li) # Calls an attribute not specifically defined on the "__init__" method line