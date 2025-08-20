import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QAction, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Hauptfenster-Einstellungen ---
        self.setWindowTitle("MDI – Aktives Unterfenster schließen")
        self.resize(900, 600)

        # --- MDI-Bereich (Multi Document Interface) ---
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        # --- Menüleiste erstellen ---
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Datei')

        # Aktion: Neues Unterfenster erstellen
        newAct = QAction('Neu', self)
        newAct.triggered.connect(self.newSubWindow)
        fileMenu.addAction(newAct)

        # Aktion: Aktives Unterfenster schließen
        closeAct = QAction('Schließen', self)
        closeAct.triggered.connect(self.closeSubWindow)
        fileMenu.addAction(closeAct)

    def newSubWindow(self):
        """Erstellt ein neues Unterfenster mit Texteditor."""
        sub = QMdiSubWindow()
        sub.setWidget(QTextEdit())
        sub.setWindowTitle("Unterfenster")
        self.mdi.addSubWindow(sub)
        sub.show()

    def closeSubWindow(self):
        """Schließt nur das aktuell aktive Unterfenster.
        activeSubWindow() liefert das Fenster, das gerade den Fokus hat.
        """
        activeSubWindow = self.mdi.activeSubWindow()
        if activeSubWindow:
            activeSubWindow.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
