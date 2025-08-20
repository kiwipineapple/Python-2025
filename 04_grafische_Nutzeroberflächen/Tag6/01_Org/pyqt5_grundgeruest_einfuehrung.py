# ------------------------------------------------------
# sys ist ein Standardmodul in Python.
# Es wird hier verwendet, um das Programm beim Schließen
# vollständig zu beenden (sys.exit) und um Kommandozeilen-
# argumente (sys.argv) an die QApplication weiterzugeben.
# ------------------------------------------------------
import sys


# Qt stellt vordefinierte Konstanten bereit,
# zum Beispiel für Maus- und Tastaturereignisse:
# Qt.LeftButton = linke Maustaste
# Qt.RightButton = rechte Maustaste
# Qt.Key_Return = Enter-Taste
# Wir nutzen diese Konstanten z.B. in der Methode mousePressEvent,
# um zu erkennen, welche Taste geklickt wurde.
from PyQt5.QtCore import Qt

# ------------------------------------------------------
# Wir importieren hier die wichtigsten Klassen für unsere grafische Oberfläche:
# - sichtbare Widgets wie Fenster, Buttons, Texteingabe usw.
# - Layouts zur Anordnung der Elemente
# - und QApplication, die gesamte GUI-Anwendung verwaltet.
# ------------------------------------------------------

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QWidget
)


# ------------------------------------------------------
# Wir definieren unsere eigene Fensterklasse "MainWindow".
# Sie erbt von QMainWindow (aus PyQt5), d.h. sie hat alle Grundfunktionen eines Fensters.
# In dieser Klasse legen wir fest, welche Elemente (Widgets) im Fenster erscheinen
# und wie sie reagieren (z.B. auf Mausklicks oder Button-Events).
# ------------------------------------------------------
# ------------------------------------------------------

# QMainWindow ist die empfohlene Hauptklasse für komplexere Fenster in PyQt5.
# Sie bringt schon viele Standardfunktionen mit, z.B.:
# - Menüleiste (menuBar)
# - Werkzeugleiste (ToolBar)
# - Statusleiste (StatusBar)
# - zentrales Inhaltsfeld (setCentralWidget)
# ------------------------------------------------------

class MainWindow(QMainWindow):
    def __init__(self):
        # ------------------------------------------------------
        # Wir rufen den Konstruktor der Elternklasse QMainWindow auf.
        # Dadurch wird das Hauptfenster korrekt initialisiert – mit allen
        # eingebauten Funktionen wie Menüleiste, Statusleiste, etc.
        #
        # Ohne diesen Aufruf würden wichtige Grundfunktionen fehlen.
        # super() sorgt dafür, dass die Elternklasse korrekt „gestartet“ wird.
        # ------------------------------------------------------

        super().__init__()

        # Fenster-Titel setzen (sichtbar oben im Fensterrahmen)
        self.setWindowTitle('PyQt5 Einführung')

        # Fenstergröße und Position auf dem Bildschirm setzen (x, y, Breite, Höhe)
        self.setGeometry(100, 100, 400, 250)

        # --- Zentrales Widget und Layout erstellen ---
        # Das zentrale Widget ist der Hauptinhalt des Fensters
        central_widget = QWidget()

        # QVBoxLayout = vertikales Layout → Widgets untereinander anordnen
        layout = QVBoxLayout()

        # --- WIDGETS ERSTELLEN ---

        # Label für Mausklick-Information (wird durch Mausereignis aktualisiert)
        self.mouse_info = QLabel('Klicke mit der Maus ins Fenster', self)

        # Beschriftung für Eingabefeld
        self.label = QLabel('Dein Name:', self)

        # Textfeld zur Eingabe des Namens
        self.line_edit = QLineEdit(self)

        # Button, um Eingabe zu bestätigen
        self.button = QPushButton('Anzeigen', self)

        # Ergebnis-Label, das nach Klick den Text zeigt
        self.result_label = QLabel('', self)

        # --- SIGNAL UND SLOT VERBINDEN ---
        # Der Button sendet beim Klicken ein Signal → verbunden mit unserer Methode
        self.button.clicked.connect(self.show_name)

        # --- WIDGETS DEM LAYOUT HINZUFÜGEN ---
        layout.addWidget(self.mouse_info)
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)

        # Layout dem zentralen Widget zuweisen
        central_widget.setLayout(layout)

        # Zentrales Widget ins Fenster einfügen
        self.setCentralWidget(central_widget)

    # --- SLOT-FUNKTION ---
    # Diese Funktion wird aufgerufen, wenn der Button gedrückt wird
    def show_name(self):
        name = self.line_edit.text() # Text aus Eingabefeld holen
        self.result_label.setText(f'Hallo, {name}!') # Begrüßung anzeigen

    # ------------------------------------------------------
    # EREIGNISBEHANDLUNG (EVENT HANDLER)
    # ------------------------------------------------------
    # Diese Methode wird automatisch aufgerufen, wenn man im Fenster mit der Maus klickt.
    # Wir „überschreiben“ damit das Standardverhalten von PyQt5 (Normalerweise passiert beim Mausklick nichts Besonderes).
    # Über das Event-Objekt erhalten wir Informationen über den Mausklick (z.B. Position, Taste).
    def mousePressEvent(self, event):
        # Wenn linke Maustaste gedrückt wurde
        if event.button() == Qt.LeftButton:
            self.mouse_info.setText(
                f'Linke Maustaste gedrückt bei ({event.x()}, {event.y()})'
            )
        # Wenn rechte Maustaste gedrückt wurde
        elif event.button() == Qt.RightButton:
            self.mouse_info.setText(
                f'Rechte Maustaste gedrückt bei ({event.x()}, {event.y()})'
            )


# --- START DER ANWENDUNG ---
# ------------------------------------------------------
# QApplication ist das zentrale Steuerobjekt für jede PyQt-Anwendung.
# Es wird genau EINMAL am Anfang erstellt
# - Es startet die Ereignisschleife (damit Fenster offen bleiben)
# - Es verarbeitet Benutzeraktionen (z.B. Klicks, Tasteneingaben)
# - Es koordiniert die Darstellung aller Fenster und Widgets

# sys.argv übergibt mögliche Kommandozeilenargumente an Qt,
# z.B. '--style=Fusion' oder '--platform=windows'.
# Auch wenn man keine Argumente nutzt, sollte man sys.argv mitgeben,
# damit Qt intern korrekt initialisiert werden kann.
# ------------------------------------------------------
app = QApplication(sys.argv)      # Erstelle die QApplication (muss immer vorhanden sein)


window = MainWindow()             # Erstelle das Fenster

window.show()                     # Zeige das Fenster


# ------------------------------------------------------
# app.exec_() startet die Ereignisschleife (Event Loop).
# → Diese Schleife hält das Fenster offen und verarbeitet alle Benutzeraktionen.

# Die Schleife läuft so lange, bis das Fenster geschlossen wird.
# Wenn das passiert, gibt exec_() eine "Exit-Nummer" zurück
# (z.B. 0 für "alles okay", oder eine Fehlernummer).

# sys.exit(...) beendet dann das Python-Programm vollständig
# und gibt diese Nummer an das Betriebssystem weiter.
#
# Merksatz: Zuerst führen wir aus (exec_), dann schließen wir sauber (exit).
# ------------------------------------------------------
sys.exit(app.exec_())



















# ------------------------------------------------------
# WICHTIGE EVENT-METHODEN IN PYQT5 (automatisch erkannt)
# ------------------------------------------------------
# Diese Methoden kann man in eigenen Klassen überschreiben,
# damit das Fenster oder ein Widget auf bestimmte Ereignisse reagiert.

#  mousePressEvent(self, event)
#      → Wird aufgerufen, wenn eine Maustaste gedrückt wird.

#  mouseReleaseEvent(self, event)
#      → Wird aufgerufen, wenn die Maustaste losgelassen wird.

#  mouseDoubleClickEvent(self, event)
#      → Wird aufgerufen beim Doppelklick mit der Maus.

#  keyPressEvent(self, event)
#      → Wird aufgerufen, wenn eine Taste auf der Tastatur gedrückt wird.

#  resizeEvent(self, event)
#      → Wird aufgerufen, wenn das Fenster in der Größe verändert wird.

#  closeEvent(self, event)
#      → Wird aufgerufen, wenn das Fenster geschlossen wird.

#  enterEvent(self, event)
#      → Wird aufgerufen, wenn die Maus in das Widget hineingeht.

#  leaveEvent(self, event)
#      → Wird aufgerufen, wenn die Maus das Widget verlässt.

# HINWEIS:
# Die Methodennamen sind festgelegt und müssen exakt so heißen,
# sonst werden sie von PyQt5 nicht automatisch aufgerufen.
# ------------------------------------------------------


