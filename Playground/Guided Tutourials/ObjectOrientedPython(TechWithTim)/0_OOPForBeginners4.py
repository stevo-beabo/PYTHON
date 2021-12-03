## Video 0 OOP in Python for Beginners (https://www.youtube.com/watch?v=JeznW_7DlB0)

class Person:
	number_of_people = 0 # This is a class-only attribute. It can only be reference to the class itself and does not change per instance of the class

	def __init__(self, name):
		self.name = name
		Person.add_person()

	@classmethod # Decorates the function as a "classmethod" that reference the class and not referencing itself
	def number_of_people_func(cls):
		return cls.number_of_people

	@classmethod
	def add_person(cls):
		cls.number_of_people +=1

p1 = Person("Tim")
print(Person.number_of_people)
p2 = Person("Jill")
print(Person.number_of_people)
print(Person.number_of_people_func())

class Math:
	@staticmethod # Static methods are basic functions but can't change
	def add5(x):
		return x + 5

	@staticmethod # Static methods are basic functions but can't change
	def add10(x):
		return x + 10

	@staticmethod # Static methods are basic functions but can't change
	def pr():
		print("print string")

print(Math.add5(5))
print(Math.add10(5))
Math.pr()