import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Schließen Method')
        self.setGeometry(100, 100, 400, 250)

        self.button = QPushButton('Fenster schließen', self)
        self.button.clicked.connect(self.close_window)

    def close_window(self):
        self.close()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
