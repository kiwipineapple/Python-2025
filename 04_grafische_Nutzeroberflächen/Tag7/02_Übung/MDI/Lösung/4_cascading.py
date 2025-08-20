import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QAction, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Hauptfenster-Setup ---
        self.setWindowTitle("MDI – Kacheln & Kaskadieren")
        self.resize(900, 600)

        # --- MDI-Bereich als zentralen Bereich ---
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        # --- Menüleiste / Datei-Menü ---
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Datei')

        # Neu
        newAct = QAction('Neu', self)
        newAct.triggered.connect(self.newSubWindow)
        fileMenu.addAction(newAct)

        # Kacheln (nebeneinander anordnen)
        tileAct = QAction('Kacheln', self)
        tileAct.triggered.connect(self.mdi.tileSubWindows)
        fileMenu.addAction(tileAct)

        # Kaskadieren (überlappend staffeln)
        cascadeAct = QAction('Kaskadieren', self)
        cascadeAct.triggered.connect(self.mdi.cascadeSubWindows)
        fileMenu.addAction(cascadeAct)

    def newSubWindow(self):
        """Neues Unterfenster mit einfachem Texteditor."""
        sub = QMdiSubWindow()
        sub.setWidget(QTextEdit())
        sub.setWindowTitle("Unterfenster")
        self.mdi.addSubWindow(sub)
        sub.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
