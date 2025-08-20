import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QAction, QTextEdit, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Erstellen eines MDI-Bereichs
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        # Menüleiste erstellen
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Datei')

        # Aktion zum Öffnen eines neuen Text-Editors
        newAct1 = QAction('Text Editor', self)
        newAct1.triggered.connect(self.newTextEditor)
        fileMenu.addAction(newAct1)

        # Aktion zum Öffnen eines neuen Labels
        newAct2 = QAction('Label', self)
        newAct2.triggered.connect(self.newLabel)
        fileMenu.addAction(newAct2)

    def newTextEditor(self):
        # Erstellen eines neuen Unterfensters mit einem Texteditor
        sub = QMdiSubWindow()
        sub.setWidget(QTextEdit())  # QTextEdit()
        sub.setWindowTitle("Text Editor")
        self.mdi.addSubWindow(sub)
        sub.show()

    def newLabel(self):
        # Erstellen eines neuen Unterfensters mit einem Label
        sub = QMdiSubWindow()
        sub.setWidget(QLabel("Das ist ein Label"))
        sub.setWindowTitle("Label")
        self.mdi.addSubWindow(sub)
        sub.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
