# importing required librarie
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt
  
  
class CurrentTime(QWidget):
  
    def __init__(self):
        super().__init__()
  
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
  
    # method called by timer
    def showTime(self):
  
        get_curr_time = QTime.currentTime()
        curr_time = get_curr_time.toString('hh:mma')
  
        # showing it to the label
        print(curr_time)
        return curr_time

# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = CurrentTime()
  
# showing all the widgets
window.showTime()
window
  
# start the app
App.exit(App.exec_())