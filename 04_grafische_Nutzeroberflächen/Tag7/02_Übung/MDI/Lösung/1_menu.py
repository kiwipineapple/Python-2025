import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit , QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Grund-Setup fürs Hauptfenster ---
        self.setWindowTitle("MDI – Einfaches Beispiel")
        self.resize(900, 600)

        # Erstellen eines MDI-Bereichs
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        # Menüleiste erstellen
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Datei')

        """
        # Aktion zum Öffnen eines neuen Unterfensters
        newAct = QAction('Neu', self)
        newAct.triggered.connect(self.newSubWindow)
        fileMenu.addAction(newAct)
        
        QAction verwendet, um die Aktion zu erstellen, bevor wir Menü hinzufüge. 
        Dies ermöglicht es, zusätzliche Eigenschaften oder Signale für die Aktion festzulegen, 
        bevor sie hinzugefügt wird. Dennoch kann fileMenu.addAction direkt verwendet werden, 
        wenn keine zusätzlichen Einstellungen benötigt werden.
        """

        # Aktion zum Öffnen eines neuen Unterfensters direkt zum Menü hinzufügen
        fileMenu.addAction('Neu', self.newSubWindow)

    def newSubWindow(self):
        # Erstellen eines neuen Unterfensters mit einem Texteditor
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
