import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()  # GUI aufbauen

    def init_ui(self):
        # --- ZENTRALES WIDGET ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # --- HAUPTLAYOUT: VERTIKAL ---
        # VBox = von oben nach unten. Darin verschachteln wir zwei horizontale Zeilen.
        main_layout = QVBoxLayout()

        # --- OBERES & UNTERES LAYOUT: HORIZONTAL ---
        # HBox = von links nach rechts (jede ist eine "Zeile").
        top_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        # --- WIDGETS ERSTELLEN ---
        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")
        btn3 = QPushButton("Button 3")
        btn4 = QPushButton("Button 4")
        btn5 = QPushButton("Button 5")

        # --- OBERES LAYOUT BEFÜLLEN ---
        top_layout.addWidget(btn1)
        top_layout.addWidget(btn2)
        top_layout.addWidget(btn3)

        # --- FLEXIBLER ABSTAND ZWISCHEN OBERER UND UNTERER ZEILE ---
        # addStretch() im VERTIKALEN Hauptlayout sorgt dafür,
        # dass die untere Zeile nach unten "gedrückt" wird.
        # (So sieht man klar: oben eine Zeile, unten eine Zeile.)
        # Wenn du den Effekt nicht willst, kommentiere die folgende Zeile aus.
        main_layout.addLayout(top_layout)
        main_layout.addStretch()  # ← Abstand, wächst/ schrumpft mit dem Fenster

        # --- UNTERES LAYOUT BEFÜLLEN ---
        bottom_layout.addWidget(btn4)
        bottom_layout.addWidget(btn5)

        # --- LAYOUTS ZUSAMMENSETZEN ---
        main_layout.addLayout(bottom_layout)

        # --- LAYOUT ZUWEISEN ---
        central_widget.setLayout(main_layout)

        self.setWindowTitle("Kombiniertes Layout – VBox mit zwei HBox-Zeilen")
        self.resize(420, 240)
        self.show()

# --- HAUPTPROGRAMM ---
app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())
