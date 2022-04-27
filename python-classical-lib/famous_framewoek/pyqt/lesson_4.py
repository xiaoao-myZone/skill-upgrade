from PyQt5.QtWidgets import QDialog, QDial, QSpinBox, QHBoxLayout
from PyQt5.QtWidgets import QApplication


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)

        dial.valueChanged.connect(spinbox.setValue)
        spinbox.valueChanged.connect(dial.setValue)

        self.setWindowTitle("Signals abd Slots")


app = QApplication([])
form = Form()
form.show()
app.exec()
