# ----- Standard-Python-Bibliothek -----
# 'sys' wird hier verwendet, um:
# 1. Beim Start Programmargumente zu lesen (sys.argv) – nötig für QApplication.
# 2. Am Ende das Programm mit sys.exit(...) sauber zu beenden.
import sys

# ----- PyQt5-Bibliotheken -----
from PyQt5.QtWidgets import (
    QApplication,   # Startpunkt jeder PyQt-Anwendung, verwaltet die Ereignisschleife
    QMainWindow,    # Hauptfenster-Klasse mit Menüleiste, Werkzeugleisten, Statusleiste und zentralem Bereich
    QMdiArea,       # Container für mehrere Unterfenster (MDI: Multi Document Interface)
    QMdiSubWindow,  # Einzelnes Unterfenster innerhalb der QMdiArea
    QTextEdit       # Einfaches Textbearbeitungsfeld (mehrzeilig)
)


class MDIExample(QMainWindow):
    def __init__(self):
        super().__init__()

        # MDI-Bereich erstellen
        self.mdi = QMdiArea()

        # QMdiArea als zentrales Widget im QMainWindow setzen
        # In QMainWindow darf es nur EIN zentrales Widget geben.
        # → Komposition: QMainWindow enthält (hat-ein) QMdiArea.
        # (Es ist kein Vererbung-sehe zusatzfolie zur Komposition in OOP)
        self.setCentralWidget(self.mdi)

        # Fenster-Titel setzen
        self.setWindowTitle("MDI – Grundlagen")

        # Menüleiste erstellen
        # In PyQt5 wird die Menüleiste nicht als Teil des zentralen Widgets (wie dem MDI-Bereich) hinzugefügt,
        # sondern ist eine eigene Komponente des QMainWindow.
        # Sie bietet einen konsistenten, leicht zugänglichen Ort für anwendungsweite Funktionen,
        # unabhängig davon, was im zentralen Widget angezeigt wird.
        self.create_menu()

        # Beispiel-Dokumente erstellen
        self.create_documents()

    def create_menu(self):
        """
          Erstellt die Menüleiste (oberer Bereich im Hauptfenster) mit dem Menü 'Datei'.
          Fügt zwei Menübefehle hinzu:
          - 'Neues Dokument' zum Öffnen eines neuen Unterfensters
          - 'Beenden' zum Schließen der gesamten Anwendung
          """

        # Menüleiste des Hauptfensters abrufen.
        # QMainWindow stellt automatisch eine Menüleiste bereit, die man mit menuBar() ansprechen kann.
        menubar = self.menuBar()

        # Ein neues Menü mit der Beschriftung 'Datei' zur Menüleiste hinzufügen.
        # In vielen Programmen enthält 'Datei' grundlegende Befehle wie Neu, Öffnen, Speichern, Beenden.
        file_menu = menubar.addMenu('Datei')

        # --- Menüpunkt: Neues Dokument ---
        # Fügt einen neuen Eintrag 'Neues Dokument' zum Datei-Menü hinzu.
        new_action = file_menu.addAction('Neues Dokument')

        # Verbindet das Signal 'triggered' (wird gesendet, wenn der Menüpunkt angeklickt wird)
        # mit der Methode self.create_document, die ein neues Unterfenster im MDI-Bereich erstellt.
        new_action.triggered.connect(self.create_document)

        # --- Menüpunkt: Beenden ---
        # Fügt einen neuen Eintrag 'Beenden' zum Datei-Menü hinzu.
        exit_action = file_menu.addAction('Beenden')

        # Verbindet das 'triggered'-Signal dieses Menüpunktes mit der Methode self.close,
        # die das Hauptfenster (und damit die gesamte Anwendung) schließt.
        exit_action.triggered.connect(self.close)

    def create_document(self):
        """
        Erstellt ein einzelnes Unterfenster mit einem QTextEdit (Textbearbeitungsfeld).
        """

        # QMdiSubWindow ist ein "Unterfenster", das in der QMdiArea liegt.
        sub_window = QMdiSubWindow()
        # Titel des Unterfensters
        sub_window.setWindowTitle('Dokument')
        # QTextEdit als Inhalt setzen
        sub_window.setWidget(QTextEdit())

        # Unterfenster der MDI-Area hinzufügen
        self.mdi.addSubWindow(sub_window)
        # Unterfenster sichtbar machen
        sub_window.show()

    def create_documents(self):
        # Erstelle mehrere Dokumente bei Programmstart
        for i in range(6):
            self.create_document()


if __name__ == '__main__':
    # QApplication ist notwendig, um eine PyQt-Anwendung zu starten.
    app = QApplication(sys.argv)

    # Hauptfenster erzeugen und anzeigen
    window = MDIExample()

    # Setzt die Startgröße des Fensters auf 800 Pixel Breite und 600 Pixel Höhe
    window.resize(800, 600)

    # Hauptfenster anzeigen
    window.show()

    # Ereignisschleife starten (Warten auf Benutzeraktionen)
    sys.exit(app.exec_())
