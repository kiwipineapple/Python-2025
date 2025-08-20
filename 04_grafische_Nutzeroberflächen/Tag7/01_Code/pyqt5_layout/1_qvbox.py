import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton

# --- HAUPTFENSTER-KLASSE ---
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui() # Benutzeroberfläche aufbauen

    def init_ui(self):
        # --- ZENTRALES WIDGET ---
        # Ein QMainWindow benötigt ein zentrales Widget, in dem alle Inhalte angezeigt werden.
        # Ohne ein zentrales Widget können wir kein Layout setzen.
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Erstellen eines vertikalen Layouts
        # QVBoxLayout = ordnet Widgets VERTIKAL (von oben nach unten) an.
        vbox = QVBoxLayout()

        # --- WIDGETS ERSTELLEN ---
        btn1 = QPushButton('Button 1')
        btn2 = QPushButton('Button 2')
        btn3 = QPushButton('Button 3')


        # --- WIDGETS ZUM LAYOUT HINZUFÜGEN ---
        # Die Reihenfolge hier bestimmt die Position im Layout (oben nach unten).

        vbox.addWidget(btn1)
        # vbox.addWidget(btn3)
        vbox.addWidget(btn2)

        # --- FLEXIBLER ABSTAND ---
        # addStretch() fügt dem Layout einen unsichtbaren, "dehnbaren" Bereich hinzu.
        # Dieser Bereich nimmt automatisch den gesamten verfügbaren Platz ein, der
        # übrig bleibt, wenn das Fenster vergrößert oder verkleinert wird.
        #
        # Wirkung:
        # - Widgets, die VOR dem addStretch() hinzugefügt werden, bleiben am oberen Rand.
        # - Widgets, die NACH dem addStretch() hinzugefügt werden, rutschen nach unten.

        # Anwendung:
        # Das ist nützlich, wenn man bestimmte Elemente (z.B. Buttons) an den unteren Rand
        # "drücken" will, ohne manuell Abstände oder feste Größen zu setzen.

        # https://www.tutorialspoint.com/pyqt/pyqt_qboxlayout_class.htm
        # In QHBoxLayout funktioniert es genauso – nur verschiebt es Elemente nach rechts.
        vbox.addStretch()

       # vbox.addStretch()

        vbox.addWidget(btn3)


        # --- LAYOUT MIT DEM ZENTRALEN WIDGET VERKNÜPFEN ---
        central_widget.setLayout(vbox)

        # --- FENSTER-EIGENSCHAFTEN ---
        self.setWindowTitle('QVBoxLayout Beispiel')
        self.resize(300, 200)  # Breite, Höhe
        self.show()


# --- HAUPTPROGRAMM ---
app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())
