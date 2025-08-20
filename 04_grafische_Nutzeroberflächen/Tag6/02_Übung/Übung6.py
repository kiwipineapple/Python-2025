import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dropdown Menü')
        self.setGeometry(200, 200, 300, 200)

        combobox = QComboBox(self)
        combobox.addItems(['Frühstück', 'Mittagessen', 'Abendessen'])
        combobox.currentTextChanged.connect(self.auswahl_anzeige)
        combobox.move(50, 50)

    def auswahl_anzeige(self, s):
        print('Auswahl ist: ', s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
