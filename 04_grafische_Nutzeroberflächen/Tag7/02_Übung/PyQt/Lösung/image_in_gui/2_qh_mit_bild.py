import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap


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

        # Laden und Hinzufügen der Bilder
        pixmap1 = QPixmap('bild1.jpg')
        pixmap2 = QPixmap('bild2.jpg')
        pixmap3 = QPixmap('bild3.jpg')

        label1 = QLabel()
        label1.setPixmap(pixmap1)

        label2 = QLabel()
        label2.setPixmap(pixmap2)

        label3 = QLabel()
        label3.setPixmap(pixmap3)

        # Hinzufügen der Bild-Labels zum horizontalen Layout
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)

        # Setzen des Layouts für das zentrale Widget
        central_widget.setLayout(hbox)

        self.setWindowTitle('Bilder nebeneinander anzeigen')
        self.resize(800, 600)
        self.show()


app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec_())
