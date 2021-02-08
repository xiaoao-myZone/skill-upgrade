from __future__ import division
import sys
import traceback
from PyQt5.QtWidgets import QApplication, QDialog, QTextBrowser, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.broswer = QTextBrowser() # display
        self.lineedit = QLineEdit("Type an expression and press Enter") # input
        self.lineedit.selectAll() # ctr + a
        layout = QVBoxLayout() # a frame with 'X' and '--' and '[]'
        layout.addWidget(self.broswer)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            text = str(self.lineedit.text())
            self.broswer.append("%s = <b>%s</b>" % (text, eval(text))) # when fresh the list in broswer
        except Exception:
            traceback.print_exc()
            self.broswer.append("<font color=red>%s is invalid</font>" % text)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
