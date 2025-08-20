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

        grid = QGridLayout()

        for i in range(3):
            for n in range(3):
                btn = QPushButton(f'Button {i} {n}')
                grid.addWidget(btn, i, n)

        central_widget.setLayout(grid)

        self.setWindowTitle('Rasterlayout')
        self.resize(500, 300)
        self.show()


app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())
