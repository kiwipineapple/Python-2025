import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Erstelle ein zentrales Widget und ein Layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Erstelle ein Label
        self.label = QLabel('Hallo Welt', self)
        layout.addWidget(self.label)

        # Erstelle einen Button
        button = QPushButton('Klick mich', self)
        button.clicked.connect(self.update_label)
        layout.addWidget(button)

        self.setCentralWidget(central_widget)
        self.setWindowTitle('Label Aktualisieren')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def update_label(self):
        self.label.setText('Button geklickt!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
