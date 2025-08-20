from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QListWidget, QPushButton
import sys

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hobby-Auswahl")
        self.setGeometry(100, 100, 350, 250)

        # Zentrales Widget + Layout
        zentral_widget = QWidget()
        layout = QVBoxLayout()

        # QListWidget erstellen und Mehrfachauswahl erlauben
        self.liste = QListWidget()
        self.liste.addItems(["Lesen", "Zeichnen", "Programmieren", "Musik", "Reisen"])
        self.liste.setSelectionMode(QListWidget.MultiSelection)

        # Button erstellen
        self.button = QPushButton("Ausgewählte anzeigen")
        self.button.clicked.connect(self.zeige_auswahl)

        # Widgets zum Layout hinzufügen
        layout.addWidget(self.liste)
        layout.addWidget(self.button)

        zentral_widget.setLayout(layout)
        self.setCentralWidget(zentral_widget)

    def zeige_auswahl(self):
        # Gibt alle ausgewählten Einträge im Terminal aus
        ausgewaehlt = self.liste.selectedItems()
        for item in ausgewaehlt:
            print("Ausgewählt:", item.text())

app = QApplication(sys.argv)
window = Fenster()
window.show()
sys.exit(app.exec_())
