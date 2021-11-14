## Video 0 OOP in Python for Beginners (https://www.youtube.com/watch?v=JeznW_7DlB0)

# A general class that will have all of the functions that will be shared by the child classes
class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old")

	def speak(self):
		print("Um...")

# Creates a child class of the parent class "Pet" but creates functions specific to itself
class Cat(Pet):
	def __init__(self, name, age, color):
		super().__init__(name, age) # Super references the "super class" or parent class. This passes the attributes  from the "__init__" function from the parent "Pet" class to the new child "Cat" class
		self.color = color

	def speak(self):
		print("Meow")

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

# Creates a child class of the parent class "Pet" but creates functions specific to itself
class Dog(Pet):
	def speak(self):
		print("Bark")

class Fish(Pet):
	pass

p = Pet("Tim", 19)
p.speak()
p.show()
c = Cat("Bill", 34, "Brown")
c.speak()
c.show()
d = Dog("Jill", 25)
d.speak()
d.show()
f = Fish("Bubbles", 10)
f.speak()
f.show()