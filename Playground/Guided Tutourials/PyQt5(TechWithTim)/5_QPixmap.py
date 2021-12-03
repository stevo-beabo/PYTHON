## Video 5 of the PyQt5 Tutorial (https://www.youtube.com/watch?v=D0iCHFXHb_g)

# FILE CREATED BY QtDesigner

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(3, -3, 801, 471))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imgs/cat.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.cat = QtWidgets.QPushButton(self.centralwidget)
        self.cat.setGeometry(QtCore.QRect(0, 470, 391, 81))
        self.cat.setObjectName("cat")

        self.dog = QtWidgets.QPushButton(self.centralwidget)
        self.dog.setGeometry(QtCore.QRect(390, 470, 411, 81))
        self.dog.setObjectName("dog")

        self.new = QtWidgets.QPushButton(self.centralwidget)
        self.new.setGeometry(QtCore.QRect(390, 550, 411, 81))
        self.new.setObjectName("new")

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

        self.dog.clicked.connect(self.show_dog) # Connects the "dog" button to the "show_dog" function below
        self.cat.clicked.connect(self.show_cat) # Connects the "cat" button to the "show_cat" function below
        self.new.clicked.connect(self.new_pixlabel) # Connects to the "new_pixlabel" function to add a new QLabel after the initial build

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cat.setText(_translate("MainWindow", "CAT"))
        self.dog.setText(_translate("MainWindow", "DOG"))
        self.new.setText(_translate("MainWindow", "NEW"))

    # Defines a function to switch the picture in the label to the dog image
    def show_dog(self):

        self.label.setPixmap(QtGui.QPixmap("imgs/dog.jpg"))

    # Defines a function to switch the picture in the label to the cat image
    def show_cat(self):

        self.label.setPixmap(QtGui.QPixmap("imgs/cat.jpg"))

    # Adding my own function here to add QLabels after the build via a QButtonPush connection
    def new_pixlabel(self, MainWindow):

        self.new_label = QtWidgets.QLabel(self.centralwidget)
        self.new_label.setHidden(False) # New QLabels are hidden by default and require this line to be seen
        self.new_label.setGeometry(QtCore.QRect(10, 10, 250, 250))
        self.new_label.setText("")
        self.new_label.setPixmap(QtGui.QPixmap("imgs/dog.jpg"))
        self.new_label.setScaledContents(True)
        self.new_label.setObjectName("new_label")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
