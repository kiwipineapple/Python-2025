import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        hbox = QHBoxLayout()

        label1 = QLabel()
        label1.setStyleSheet("background-color: lightgreen")

        label2 = QLabel()
        label2.setStyleSheet("background-color: orange")

        label3 = QLabel()
        label3.setStyleSheet("background-color: lightpink")

        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        central_widget.setLayout(hbox)

        # --- FENSTER-EIGENSCHAFTEN ---
        self.setWindowTitle('Übung2')
        self.resize(300, 200)  # Breite, Höhe
        self.show()


# --- HAUPTPROGRAMM ---
app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())
