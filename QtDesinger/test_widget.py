import sys

#from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __int__(self):
        super().__int__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        # Set the central widget of the window
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Start the event loop.
app.exec()
