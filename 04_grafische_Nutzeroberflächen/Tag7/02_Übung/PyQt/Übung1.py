import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        vbox = QVBoxLayout()

        label1 = QLabel('Name')
        label2 = QLabel('E-Mail')
        label3 = QLabel('Telefonnummer')

        text1 = QLineEdit()
        text2 = QLineEdit()
        text3 = QLineEdit()

        vbox.addWidget(label1)
        vbox.addWidget(text1)
        vbox.addWidget(label2)
        vbox.addWidget(text2)
        vbox.addWidget(label3)
        vbox.addWidget(text3)

        central_widget.setLayout(vbox)

        self.setWindowTitle('Übung1')
        self.resize(300, 200)  # Breite, Höhe
        self.show()


app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())
