from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QComboBox, QPushButton
import sys

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dropdown-Beispiel")
        self.setGeometry(100, 100, 300, 150)

        # Zentrales Widget und Layout
        zentral_widget = QWidget()
        layout = QVBoxLayout()

        # QComboBox erstellen und befüllen
        self.combo = QComboBox()
        self.combo.addItems(["Frühstück", "Mittagessen", "Abendessen"])

        # Button erstellen
        self.button = QPushButton("Auswahl anzeigen")
        self.button.clicked.connect(self.zeige_auswahl)

        # Widgets zum Layout hinzufügen
        layout.addWidget(self.combo)
        layout.addWidget(self.button)

        # Layout dem zentralen Widget zuweisen
        zentral_widget.setLayout(layout)
        self.setCentralWidget(zentral_widget)

    def zeige_auswahl(self):
        # Gibt die aktuell gewählte Option im Terminal aus
        auswahl = self.combo.currentText()
        print(f"Gewählte Option: {auswahl}")

app = QApplication(sys.argv)
window = Fenster()
window.show()
sys.exit(app.exec_())
