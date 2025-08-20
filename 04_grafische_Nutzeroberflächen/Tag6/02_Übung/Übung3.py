import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QLineEdit)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Entry')
        self.setGeometry(100, 100, 400, 250)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(150, 50)

        self.button = QPushButton('Button klicken', self)
        self.button.move(150, 100)
        self.button.clicked.connect(self.update_label)

        self.label = QLabel('New Label', self)
        self.label.move(170, 160)

    def update_label(self):
        text = self.line_edit.text()
        self.label.setText(text)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
