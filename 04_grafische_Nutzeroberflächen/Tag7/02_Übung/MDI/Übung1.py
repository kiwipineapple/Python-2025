import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit)


class MDIExample(QMainWindow):
    def __init__(self):
        super().__init__()

        # MDI-Bereich erstellen
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.setWindowTitle("MDI-Übung1")
        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('Datei')
        new_action = file_menu.addAction('Neu')
        new_action.triggered.connect(self.create_document)

    def create_document(self):
        sub_window = QMdiSubWindow()
        sub_window.setWindowTitle('Unterfenster')
        sub_window.setWidget(QTextEdit())  # Erstellen Subwindow
        # Fügen Subwindow in MDI(Multi Dokument Interface) Container
        self.mdi.addSubWindow(sub_window)
        sub_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MDIExample()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec_())
