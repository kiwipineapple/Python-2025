import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QColor


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Erstellen eines zentralen Widgets
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Erstellen eines horizontalen Layouts
        hbox = QHBoxLayout()

        # Erstellen von Platzhalter-Bildern
        for color in [QColor('red'), QColor('green'), QColor('blue')]:
            label = QLabel()
            label.setStyleSheet(f'background-color: {color.name()};')
            hbox.addWidget(label)

        # Setzen des Layouts für das zentrale Widget
        central_widget.setLayout(hbox)

        self.setWindowTitle('Horizontaler Bilder-Viewer')
        self.show()


app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())
