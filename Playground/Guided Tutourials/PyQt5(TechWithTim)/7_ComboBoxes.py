## Video 7 of the PyQt5 Tutorial (https://www.youtube.com/watch?v=crJVzc5Ct_s)

# FILE CREATED BY QtDesigner


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboX = QtWidgets.QComboBox(self.centralwidget)
        self.comboX.setGeometry(QtCore.QRect(50, 110, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.comboX.setFont(font)
        self.comboX.setObjectName("comboX")
        self.comboX.addItem("")
        self.comboX.addItem("")
        self.comboY = QtWidgets.QComboBox(self.centralwidget)
        self.comboY.setGeometry(QtCore.QRect(480, 110, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.comboY.setFont(font)
        self.comboY.setObjectName("comboY")
        self.comboY.addItem("")
        self.comboY.addItem("")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(290, 410, 211, 121))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 290, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # An example of adding to the ComboBox and setting/resetting the default value
#        self.comboX.addItem("Hello") # Adds an item to the bottom of a combo box
#        index = self.comboX.findText("Hello", QtCore.Qt.MatchFixedString) # This will tell us where a specific item is in the combo box (starts at 0)
#        self.comboX.setCurrentIndex(index) # Sets the default value to whatever is stored in the variable "index" """

        self.submit.clicked.connect(self.pressed) # Connects the "submit" button to the "pressed" function

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboX.setItemText(0, _translate("MainWindow", "0"))
        self.comboX.setItemText(1, _translate("MainWindow", "1"))
        self.comboY.setItemText(0, _translate("MainWindow", "0"))
        self.comboY.setItemText(1, _translate("MainWindow", "1"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "X XOR Y = ")

    # Defines a function to read the values of the ComboBoxes and compare the values in the "XOR Gate" logic
    def pressed(self):
        x = int(self.comboX.currentText()) # Grabs the current value in the X ComboBox and stores it in the "x" variable
        y = int(self.comboY.currentText()) # Grabs the current value in the Y ComboBox and stores it in the "y" variable
        xor = (x and not y) or (not x and y) # Compares the values and stores the result in the "xor" variable
        # Some results from the previous comparison return a Boolean type, this statement switches them to Integer
        if xor == True:
            xor = 1
        else:
            xor = 0

        self.label.setText("X XOR Y= " + str(xor)) # Changes the Label to the result of the above comparison

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
