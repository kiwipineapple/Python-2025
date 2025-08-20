import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Erstellen eines zentralen Widgets
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Erstellen eines Rasterlayouts
        grid = QGridLayout()

        # Erstellen von Schaltflächen im Rasterlayout
        for row in range(3):
            for col in range(3):
                button = QPushButton(f'Button {row} {col}')  # Zeigt die Position im Raster an
                grid.addWidget(button, row, col)  # Zeilen und Spalten beginnen bei 0

        # Setzen des Layouts für das zentrale Widget
        central_widget.setLayout(grid)

        self.setWindowTitle('Raster von Schaltflächen mit 0-basierter Indizierung')
        self.show()


app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())
