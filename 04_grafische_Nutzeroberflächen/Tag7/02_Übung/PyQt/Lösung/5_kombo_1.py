import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel, \
    QLineEdit, QPushButton


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

        # Erstellen eines horizontalen Layouts für Schaltflächen
        hbox = QHBoxLayout()
        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')
        button3 = QPushButton('Button 3')
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3)

        # Erstellen eines Formularlayouts
        form = QFormLayout()
        name_label = QLabel('Name:')
        name_input = QLineEdit()
        email_label = QLabel('E-Mail:')
        email_input = QLineEdit()
        form.addRow(name_label, name_input)
        form.addRow(email_label, email_input)

        # Hinzufügen des horizontalen Layouts und des Formularlayouts zum vertikalen Layout
        vbox.addLayout(hbox)  # Horizontale Schaltflächenreihe oben
        vbox.addLayout(form)  # Formular darunter

        # Setzen des Layouts für das zentrale Widget
        central_widget.setLayout(vbox)

        self.setWindowTitle('Kombiniertes Layout Beispiel')
        self.show()


app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())
