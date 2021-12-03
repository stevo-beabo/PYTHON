## Video 6 of the PyQt5 Tutorial (https://www.youtube.com/watch?v=GkgMTyiLtWk)

# FILE CREATED BY QtDesigner

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(150, 150, 451, 221))
        self.button.setObjectName("button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button.clicked.connect(self.show_popup) # Connects the button click to the "show_popup" function

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button.setText(_translate("MainWindow", "Show PopUp"))

    # Defines a function to control the popup message box
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Tutorial on PyQt5") # Sets
        msg.setText("This is the main text!") # Sets the text that will appear in the popup window
        msg.setIcon(QMessageBox.Question) # Puts an icon next to your message. Critical = Red X, Warning = Yellow Triangle, Information = little i, Question = ? mark
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore) # Controls what buttons are presented on the PopUp Message
        msg.setDefaultButton(QMessageBox.Ignore) # Sets which button will be selected by default with the window pops up
        msg.setInformativeText("Informative Text, ya!") # Puts a small note at the bottom of the popup

        msg.setDetailedText("These are the details") # Adds an additional button that will display/hide further information in the popup window if pressed

        msg.buttonClicked.connect(self.popup_button) # Connects the QMessageBox buttons to the function "popup_button"

        x = msg.exec_()

    # Defines a funciton to print which button was pressed on the popup window
    def popup_button(self, i): # The "i" parameter will accept which button was clicked
        print(i.text()) # "i.text" will display only the name of the button that was clicked

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# Extra notes:
"""QMessageBox.Button options
QMessagebox.Ok
QMessagebox.Open
QMessagebox.Save
QMessagebox.Cancel
QMessagebox.Close
QMessagebox.Yes
QMessagebox.No
QMessagebox.Abort
QMessagebox.Retry
QMessagebox.Ignore"""