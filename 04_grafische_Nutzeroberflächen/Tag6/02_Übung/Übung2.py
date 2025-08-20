import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('neue Fenster')
        self.setGeometry(100, 100, 400, 250)

        central_widget = QWidget()

        layout = QVBoxLayout()

        self.button = QPushButton('Button klicken', self)
        # self.button.move(150, 100)

        self.button.clicked.connect(self.update_label)
        layout.addWidget(self.button)

        self.label = QLabel('New Label', self)
        # self.label.move(150, 50)
        layout.addWidget(self.label)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def update_label(self):
        self.label.setText('geklickt!')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
