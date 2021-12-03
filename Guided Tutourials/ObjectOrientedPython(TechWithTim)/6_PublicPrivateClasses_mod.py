## Video 6 of Object Oriented Programming with Python (https://www.youtube.com/watch?v=xY__sjI5yVU)
## First script to show Public Class functionality 

class _Private: # A Private Class can only be used within the same file or scope. The "_" at the beginnig of the class name marks it as Private
	def __init__(self, name):
		self.name = name

class NotPrivate: # A Public Class can be accessed by all other classes within or outside of the file
	def __init__(self, name):
		self.name = name
		self.priv = _Private(name)

	def _display(self): # A Private Method, marked with the "_" at the beginning of the name.
		print("Hello")

	def display(self): # A Publicly usuable method
		print("Hi")

