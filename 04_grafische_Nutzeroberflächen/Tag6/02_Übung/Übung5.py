import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QRadioButton, QLabel, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('radio')
        self.setGeometry(100, 100, 400, 250)

        central_widget = QWidget()

        layout = QVBoxLayout()

        radiobutton = QRadioButton("Australia")
        # radiobutton.setChecked(True)
        radiobutton.country = "Australia"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton)

        radiobutton = QRadioButton("China")
        radiobutton.country = "China"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton)

        radiobutton = QRadioButton("Japan")
        radiobutton.country = "Japan"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton)

        self.label = QLabel('Country sind nicht ausgewählt.')
        layout.addWidget(self.label)

        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.label.setText("Country is %s" % (radioButton.country))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
