from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton
import sys

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Textausgabe")
        self.setGeometry(100, 100, 400, 250)

        zentral_widget = QWidget()
        layout = QVBoxLayout()

        # QTextEdit für mehrzeilige Texteingabe
        self.textfeld = QTextEdit()

        # Button zur Anzeige des eingegebenen Textes
        self.button = QPushButton("Text anzeigen")
        self.button.clicked.connect(self.zeige_text)

        layout.addWidget(self.textfeld)
        layout.addWidget(self.button)

        zentral_widget.setLayout(layout)
        self.setCentralWidget(zentral_widget)

    def zeige_text(self):
        # Gibt den eingegebenen Text im Terminal aus
        eingabe = self.textfeld.toPlainText()
        print("Eingegebener Text:\n", eingabe)

app = QApplication(sys.argv)
window = Fenster()
window.show()
sys.exit(app.exec_())
