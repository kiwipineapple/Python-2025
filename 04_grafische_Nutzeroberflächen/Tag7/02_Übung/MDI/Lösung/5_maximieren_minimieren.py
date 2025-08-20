import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QAction, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Hauptfenster-Setup  ---
        self.setWindowTitle("MDI – Maximieren/Minimieren (aktives Unterfenster)")
        self.resize(900, 600)

        # --- MDI-Bereich als zentralen Bereich ---
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        # --- Menü: Datei ---
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Datei')

        # Neu (Unterfenster mit Texteditor)
        newAct = QAction('Neu', self)
        newAct.triggered.connect(self.newSubWindow)
        fileMenu.addAction(newAct)

        # Maximieren (nur aktives Unterfenster)
        maxAct = QAction('Maximieren', self)
        maxAct.triggered.connect(self.maximizeSubWindow)
        fileMenu.addAction(maxAct)

        # Minimieren (nur aktives Unterfenster)
        minAct = QAction('Minimieren', self)
        minAct.triggered.connect(self.minimizeSubWindow)
        fileMenu.addAction(minAct)

    def newSubWindow(self):
        sub = QMdiSubWindow()
        sub.setWidget(QTextEdit())
        sub.setWindowTitle("Unterfenster")
        self.mdi.addSubWindow(sub)
        sub.show()

    def maximizeSubWindow(self):
        activeSubWindow = self.mdi.activeSubWindow()
        if activeSubWindow:
            activeSubWindow.showMaximized()

    def minimizeSubWindow(self):
        activeSubWindow = self.mdi.activeSubWindow()
        if activeSubWindow:
            activeSubWindow.showMinimized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
