import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Erstelle einen Button
        btn = QPushButton('Schließen', self)
        btn.move(50, 50)
        btn.clicked.connect(self.close)  # Verbinde das Klick-Ereignis mit der close Methode

        self.setWindowTitle('Einfaches Fenster mit Button')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
