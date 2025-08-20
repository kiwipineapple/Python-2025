import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Erstelle ein zentrales Widget und ein Layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Erstelle ein Textfeld
        self.text_field = QLineEdit(self)
        layout.addWidget(self.text_field)

        # Erstelle ein Label
        self.label = QLabel('', self)
        layout.addWidget(self.label)

        # Erstelle einen Button
        button = QPushButton('Zeige Text', self)
        button.clicked.connect(self.show_text)
        layout.addWidget(button)

        self.setCentralWidget(central_widget)
        self.setWindowTitle('Textfeld und Button')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def show_text(self):
        self.label.setText(self.text_field.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
