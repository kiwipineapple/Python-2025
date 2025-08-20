import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton

# --- HAUPTFENSTER-KLASSE ---
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui() # Benutzeroberfläche aufbauen

    def init_ui(self):
        # --- ZENTRALES WIDGET ---
        # Ein QMainWindow braucht ein zentrales Widget, um Layouts und Inhalte anzuzeigen.
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # --- HORIZONTALES LAYOUT ---
        # QHBoxLayout = ordnet Widgets HORIZONTAL (von links nach rechts) an.
        hbox = QHBoxLayout()

        # --- WIDGETS ERSTELLEN ---
        btn1 = QPushButton('Button 1')
        btn2 = QPushButton('Button 2')
        btn3 = QPushButton('Button 3')

        # --- WIDGETS HINZUFÜGEN ---
        # Die Reihenfolge hier bestimmt die Position (von links nach rechts).
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        #hbox.addWidget(btn3)

        # --- FLEXIBLER ABSTAND ---
        # addStretch() fügt einen "dehnbaren" Bereich hinzu.
        # Alles, was danach kommt, wird an den rechten Rand geschoben.
        hbox.addStretch()

        hbox.addWidget(btn3)

        # Setzen des Layouts für das zentrale Widget
        central_widget.setLayout(hbox)

        # --- FENSTER-EIGENSCHAFTEN --
        self.setWindowTitle('QHBoxLayout Beispiel')
        self.resize(300, 100)  # Breite, Höhe
        self.show()


app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())
