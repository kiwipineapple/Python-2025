import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QCheckBox, QLabel, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Checkbox')
        self.setGeometry(100, 100, 400, 250)

        central_widget = QWidget()

        layout = QVBoxLayout()

        self.checkbox1 = QCheckBox('Checkbox1', self)
        self.checkbox1.stateChanged.connect(self.update_label)

        self.checkbox2 = QCheckBox('Checkbox2', self)
        self.checkbox2.stateChanged.connect(self.update_label)

        self.label = QLabel('Checkbox sind nicht ausgewählt.')

        layout.addWidget(self.checkbox1)
        layout.addWidget(self.checkbox2)
        layout.addWidget(self.label)

        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def update_label(self):
        check1 = self.checkbox1.isChecked()
        check2 = self.checkbox2.isChecked()
        self.label.setText(
            f'Checkbox1 ist {check1}, Checkbox2 ist {check2}')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
