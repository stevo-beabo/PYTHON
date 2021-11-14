## Video 3 of Object Oriented Programming with Python (https://www.youtube.com/watch?v=H2SQrZK2nvM)

# Example 1
class Dog(object):
	def __init__(self, name, age):
		self.name = name 
		self.age = age

	def speak(self):
		print("Hi I am", self.name, "and I am", self.age, "years old")

	def talk(self):
		print("Bark!")


class Cat(Dog):
	def __init__(self, name, age, color):
		super().__init__(name, age) # "super" is referring to the parent/super class "Dog()" and it's "__init__" method
		self.color = color # Adds the attribute "color" for the "Cat" class that does not exist in the parent class

	def talk(self):
		print("Meow!")


jim = Dog("jim", 70)
jim.speak()
jim.talk()

tim = Cat("tim", 5, "blue") # Attributes "name" & "age" are being inherited from the parent/super class but "color" needs to be added when calling the "Cat()" child class
tim.speak() # Uses the "speak" method from the parent/super class "Dog()" with the attributes that have been passed to the "Cat" child class
tim.talk() # The method "talk" from the child class overrides the "talk" method from the parent/super class

# Example 2
class Vehicle(): # Creating a parent/super class that doesn't inherent from anything
	def __init__(self, price, gas, color):
		self.price = price
		self.gas = gas
		self.color = color

	def fillUpTank(self):
		self.gas = 100

	def emptyTank(self):
		self.gas = 0

	def gasLeft(self):
		return self.gas

class Car(Vehicle): # Class "Car" is inherenting all attributes from the parent/super class "Vehicle"
	def __init__(self, price, gas, color):
		super().__init__(price, gas, color)
		self.speed = speed # Setting a specific attribute "speed" for Car that does not exist in "Vehicle"

	def horn(self): # Creating a method that does not exist in the parent/super class
		print("beep beep")

class Truck(Car): # Class "Truck" is inheriting attributes from class "Car" so it also has the attributes that "Car" is inheritting from "Vehicle"
	def __init__(self, price, gas, color):
		super().__init__(price, gas, color)
		self.tires = tires

	def horn(self): # Customizing the specific method for the needs of the class "Truck"
		print("honk honk")
