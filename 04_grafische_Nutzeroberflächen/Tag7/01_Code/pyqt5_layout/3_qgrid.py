import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton

# --- HAUPTFENSTER-KLASSE ---
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()  # Benutzeroberfläche aufbauen

    def init_ui(self):
        # --- ZENTRALES WIDGET ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # --- RASTERLAYOUT ---
        # QGridLayout = ordnet Widgets in ZEILEN und SPALTEN an (wie eine Tabelle).
        grid = QGridLayout()

        # --- WIDGETS ERSTELLEN ---
        btn1 = QPushButton('Button 1')
        btn2 = QPushButton('Button 2')
        btn3 = QPushButton('Button 3')
        btn4 = QPushButton('Button 4')


        # --- WIDGETS HINZUFÜGEN ---
        # Syntax: addWidget(widget, zeile, spalte)
        # Indizierung beginnt bei 0 (oben links ist Zeile 0, Spalte 0)
        #grid.addWidget(btn1, 0, 0)  # Erste Zeile, erste Spalte
        #grid.addWidget(btn2, 0, 1)  # Erste Zeile, zweite Spalte
        #grid.addWidget(btn3, 1, 0)  # Zweite Zeile, erste Spalte
        #grid.addWidget(btn4, 1, 1)  # Zweite Zeile, zweite Spalte

        # --- OPTIONAL: SPANNEN ÜBER MEHRERE ZELLEN ---
        grid.addWidget(btn1, 0, 0, 1, 2)  # 1 Zeile hoch, 2 Spalten breit
        grid.addWidget(btn2, 1, 0)  # Moved to next row
        grid.addWidget(btn3, 1, 1)
        grid.addWidget(btn4, 2, 0)


        # --- LAYOUT ZUWEISEN ---
        central_widget.setLayout(grid)

        # --- FENSTER-EIGENSCHAFTEN ---
        self.setWindowTitle('QGridLayout Beispiel')
        self.resize(300, 150)
        self.show()

# --- HAUPTPROGRAMM ---
app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())


# Hinweis zu rowSpan und colSpan:
# In addWidget(widget, row, column, rowSpan, colSpan) bedeutet:
#   row, column  = Startposition im Raster (0-basierte Indizierung)
#   rowSpan      = Anzahl der Zeilen, die das Widget nach unten belegt
#   colSpan      = Anzahl der Spalten, die das Widget nach rechts belegt
#
# Wichtig:
# - Alle Zellen, die durch rowSpan/colSpan abgedeckt werden, können
#   nicht von anderen Widgets belegt werden.
# - Wenn andere Widgets in diese Zellen eingefügt werden, verschwinden sie,
#   da der Platz bereits durch das gespannte Widget reserviert ist.
# - Um alle Widgets sichtbar zu halten, müssen sie außerhalb des belegten
#   Bereichs platziert werden (andere Zeilen/Spalten verwenden).
