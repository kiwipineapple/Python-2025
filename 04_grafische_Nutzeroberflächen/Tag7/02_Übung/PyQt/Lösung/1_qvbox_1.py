import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Erstellen eines zentralen Widgets
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Erstellen eines vertikalen Layouts
        vbox = QVBoxLayout()

        # Erstellen von Beschriftungen und Eingabefeldern
        name_label = QLabel('Name:')
        name_input = QLineEdit()

        email_label = QLabel('E-Mail:')
        email_input = QLineEdit()

        phone_label = QLabel('Telefonnummer:')
        phone_input = QLineEdit()

        # Hinzufügen der Beschriftungen und Eingabefelder zum Layout
        vbox.addWidget(name_label)
        vbox.addWidget(name_input)
        vbox.addWidget(email_label)
        vbox.addWidget(email_input)
        vbox.addWidget(phone_label)
        vbox.addWidget(phone_input)

        # Setzen des Layouts für das zentrale Widget
        central_widget.setLayout(vbox)

        self.setWindowTitle('Vertikales Formular')
        self.show()


app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())
