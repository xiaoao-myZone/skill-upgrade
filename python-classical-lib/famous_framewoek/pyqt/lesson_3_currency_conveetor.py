import sys
from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QDoubleSpinBox
from PyQt5.QtWidgets import QApplication, QGridLayout


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        date = self.getdata()
        rates = sorted(self.rates.keys())

        dateLabel = QLabel(date)
        self.fromComboBox = QComboBox()  # drop menu
        self.fromComboBox.addItems(rates)
        self.fromSpinBox = QDoubleSpinBox()  # num input
        self.fromSpinBox.setRange(0.01, 10000000.00)
        self.fromSpinBox.setValue(1.00)
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates)
        self.toLabel = QLabel("1.00")

        grid = QGridLayout()
        grid.addWidget(dateLabel, 0, 0)
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        self.setLayout(grid)

        self.fromComboBox.currentIndexChanged.connect(self.updateUi)
        self.toComboBox.currentIndexChanged.connect(self.updateUi)
        self.fromSpinBox.valueChanged.connect(self.updateUi)
        self.setWindowTitle("Currency")

    def updateUi(self):
        to = str(self.toComboBox.currentText())
        from_ = str(self.fromComboBox.currentText())
        amount = (self.rates[from_]) / self.rates[to] * \
            self.fromSpinBox.value()

        self.toLabel.setText("%0.2f" % amount)

    def getdata(self):
        self.rates = {
            "China yuan": 1,
            "USA dollar": 7,
            "Japan yuan": 0.05
        }
        date = "Exchange Rates Date: " + "2021-02-08"
        return date


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec()
