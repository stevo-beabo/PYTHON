## Video 2 of the PyQt5 Tutorial (https://www.youtube.com/watch?v=-2uyzAqefyE)

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

# Creates an inherited class to control the window bases on the "QMainWindow" class
class MyWindow(QMainWindow):
	# Defines the initial function of this class
	def __init__(self):
		# Calles the parent constructor of the QMainWindow class
		super(MyWindow, self).__init__()
		# "setGeometry" sets the size and onscreen location of our window with arguments (x_position, y_position, width, height)
		# x_position and y_position refer to which pixel the upper-left corner of the window will be set 
		self.setGeometry(200, 200, 300,300)
		# "setWindowTitle" sets what will appear on the top bar of the window
		self.setWindowTitle("Basic Main Window")
		# Calls the "initUI" function that will control the Widgets inside of the "MyWindow"
		self.initUI()

	# Defines the "initUI" function with will control the Widgets nested in the window
	def initUI(self):
# Creating a Label Widget
		# Sets a variable with the QLabel function from the QtWidgets module and attaching it to the main window variable "win"
		self.label = QtWidgets.QLabel(self)
		# "setText" will control what the Label Widget displays
		self.label.setText("My First Label Widget")
		# "move" sets the position on the window our Label Widget will show up
		# Again this refers to the relative pixel of the main window
		self.label.move(50, 50)
		# "adjustSize" controlls how much space the text can take. Arguments are (width, heighth).
		# If nothing is specified it automatically adjusts to fit
		self.label.adjustSize()

# Creating a Button Widget
		# Sets a variable for the "QPushButton" function and sets it in the "win" window
		self.b1 = QtWidgets.QPushButton(self)
		# "setText" controls what is displayed on our button
		self.b1.setText("Click Me")
		# Maps the Button Widget to the "clicked" function below
		self.b1.clicked.connect(self.clicked)

	# Defines a function to control what happens when the Button Widget is clicked
	def clicked(self):
		# Changes the test of the Label Widget 
		self.label.setText("You Pressed the Button")
		# Readjusts the size of the label widget to fit the new text
		self.label.adjustSize()

def window():
	app = QApplication(sys.argv)
	# Calling the "MyWIndow" class
	win = MyWindow()
	win.show()
	sys.exit(app.exec_())

window()
