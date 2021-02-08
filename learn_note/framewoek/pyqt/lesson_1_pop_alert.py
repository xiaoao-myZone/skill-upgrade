import sys
import time
from PyQt5.QtCore import QTime, Qt, QTimer
from PyQt5.QtWidgets import QLabel, QApplication
# from PyQt5.QtGui import QApplication
print(sys.argv)
app = QApplication(sys.argv)

try:
    # due = QTime.currentTime()
    message = "Alert!"
    if len(sys.argv) < 2:
        raise ValueError
    hours, mins = sys.argv[1].split(":")
    due = QTime(int(hours), int(mins))
    if not due.isValid():
        raise ValueError
    if len(sys.argv) > 2:
        messsage = " ".join(sys.argv[2:])
except ValueError:
    message = "error"

while QTime.currentTime() < due:
    time.sleep(20)

label = QLabel("<font color=red size=72><b>" + message + "</b></font>")
# anchor the label?
label.setWindowFlags(Qt.SplashScreen) # display the label with splash method
# app has week association with widgets on the surface
label.show()
# 600000 unit is ms
QTimer.singleShot(60000, app.quit)
app.exec_()
