## Video 1 of the PyQt5 tutourial (https://www.youtube.com/watch?v=Vde5SH8e1OQ)

# This will import the relavent info from the system based on the OS being used
import sys

# Importing the needed "Q" Widget modules from the PyQt5 Libraries
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

# Simple function for creating a window
def window():
	app = QApplication(sys.argv) # Sets the basic config for the sys the code is running on
# Defining the properties of the main window
	win = QMainWindow() # Puts the imported funciton "QMainWindow" into a variable that then can then be referenced when setting further parameters
	win.setGeometry(200, 200, 300,300)	# "setGeometry" sets the size and onscreen location of our window with arguments (x_position, y_position, width, height)
										# x_position and y_position refer to which pixel the upper-left corner of the window will be set
	win.setWindowTitle("Basic Main Window") # "setWindowTitle" sets what will appear on the top bar of the window

# Creating a Label Widget to put into the main window
	label = QtWidgets.QLabel(win) # Sets a variable with the QLabel function from the QtWidgets module and attaching it to the main window variable "win"
	label.setText("My First Label Widget") # "setText" will control what the Label Widget displays
	label.move(50, 50) 	# "move" sets the position on the window our Label Widget will show up. Again this refers to the relative pixel of the main window
	label.adjustSize() 	# "adjustSize" controlls how much space the text can take. Arguments are (width, heighth). If nothing is specified it automatically adjusts to fit

	win.show() # The ".show" function is necessary becuase windows are hidden by default
	sys.exit(app.exec_()) # Controls how the application is stopped if the window is closed

window() # Calls the "window" function that we just defined above
