import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):

   def __init__(self, color):
       super(Color, self).__init__()
       self.setAutoFillBackground(True)

       palette = self.palette()
       palette.setColor(QPalette.Window, QColor(color))
       self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        self.setFixedSize(QSize(1680, 990))

        string_text = "Test"
        layout = QVBoxLayout()
        am_label = QLabel(string_text)

        am_label.setAlignment(Qt.AlignCenter)
        am_label.show()

#       layout.addWidget(Color('red'))
#       layout.addWidget(Color('green'))
#       layout.addWidget(Color('blue'))
#       layout.addWidget(Color('yellow'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

w = MainWindow()
w.show()


app.exec()
