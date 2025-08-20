import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFormLayout, QLabel, QLineEdit, QTextEdit, QPushButton


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Erstellen eines zentralen Widgets
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Erstellen eines Formularlayouts
        form = QFormLayout()

        # Erstellen von Formularfeldern
        name_label = QLabel('Name:')
        name_input = QLineEdit()

        email_label = QLabel('E-Mail-Adresse:')
        email_input = QLineEdit()

        message_label = QLabel('Nachricht:')
        message_input = QTextEdit()

        # Erstellen des Absenden-Buttons
        submit_button = QPushButton('Absenden')

        # Hinzufügen von Feldern zum Formularlayout
        form.addRow(name_label, name_input)
        form.addRow(email_label, email_input)
        form.addRow(message_label, message_input)
        form.addRow(submit_button)

        # Setzen des Layouts für das zentrale Widget
        central_widget.setLayout(form)

        self.setWindowTitle('Kontaktformular')
        self.show()


app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())
