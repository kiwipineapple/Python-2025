from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QProgressBar, QPushButton
import sys
import time

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fortschrittsanzeige")
        self.setGeometry(100, 100, 400, 150)

        # Zentrales Widget und Layout vorbereiten
        zentral_widget = QWidget()
        layout = QVBoxLayout()

        # Fortschrittsbalken erstellen und auf 0 setzen
        self.progress = QProgressBar()
        self.progress.setValue(0)

        # Button mit der Beschriftung „Datei laden“
        self.button = QPushButton("Datei laden")
        self.button.clicked.connect(self.start_progress)

        # Widgets dem Layout hinzufügen
        layout.addWidget(self.progress)
        layout.addWidget(self.button)

        # Layout dem zentralen Widget zuweisen
        zentral_widget.setLayout(layout)
        self.setCentralWidget(zentral_widget)

    def start_progress(self):
        # Fortschritt in 10 Schritten (0–100%) anzeigen
        for i in range(11):  # 0 bis 10
            self.progress.setValue(i * 10)  # Fortschritt setzen (z.B. 0, 10, 20, ..., 100)
            QApplication.processEvents()
            # Warum brauchen wir das?
            # Normalerweise wird die Benutzeroberfläche erst nach der Schleife aktualisiert.
            # Damit der Fortschrittsbalken sich SCHRITT FÜR SCHRITT sichtbar bewegt,
            # müssen wir die GUI manuell auffordern, sich zwischendurch zu aktualisieren.
            # Das machen wir mit: QApplication.processEvents()
            # Ohne diese Zeile würde der Balken erst am Ende der Schleife auf 100% springen.
            # Deaktiviere QApplication.processEvents() und beobachte das Verhalten bei time.sleep(1.0)

            time.sleep(0.5)  # Künstliche Ladezeit (halbsekündige Pause pro Schritt)

        # Nach Abschluss kann optional noch eine Meldung ausgegeben werden:
        print("Ladevorgang abgeschlossen!")

# Anwendung starten
app = QApplication(sys.argv)
window = Fenster()
window.show()
sys.exit(app.exec_())
