import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QFormLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit
)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Zentrales Widget (Container für das Layout)
        central = QWidget()
        self.setCentralWidget(central)

        # Formularlayout: links Labels, rechts Eingabefelder
        form = QFormLayout()

        # Variante A: explizit mit QLabel + QLineEdit
        name_label = QLabel("Name:")
        name_edit = QLineEdit()
        name_edit.setPlaceholderText("Vor- und Nachname")
        form.addRow(name_label, name_edit)

        # Variante B: Kurzform – Label-Text direkt als String
        email_edit = QLineEdit()
        email_edit.setPlaceholderText("beispiel@domain.de")
        form.addRow("E‑Mail:", email_edit)

        # Eingabemaske/Validierung könnte man später zeigen (z.B. nur Zahlen)
        age_edit = QLineEdit()
        age_edit.setPlaceholderText("Alter in Jahren")
        form.addRow("Alter:", age_edit)

        # Zeile ohne Label: Widget füllt die rechte Spalte (praktisch für mehrzeiligen Text)
        note_edit = QTextEdit()
        note_edit.setPlaceholderText("Nachricht / Bemerkungen …")
        form.addRow(note_edit)  # keine Label-Spalte

        # Submit-Button als Abschlusszeile
        submit_btn = QPushButton("Absenden")
        form.addRow("", submit_btn)  # leeres Label = Button rechts ausgerichtet


        central.setLayout(form)

        self.setWindowTitle("QFormLayout Beispiel")
        self.resize(420, 300)
        self.show()

app = QApplication(sys.argv)
w = MyWindow()
sys.exit(app.exec_())
