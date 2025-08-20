import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit)


class MDIExample(QMainWindow):
    def __init__(self):
        super().__init__()

        # MDI-Bereich erstellen
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.setWindowTitle("MDI-Übung3")
        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('Datei')
        new_action = file_menu.addAction('Neu')
        new_action.triggered.connect(self.create_document)

        exit_action = file_menu.addAction("Beenden")
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close_active_subwindow)

    def create_document(self):
        sub_window = QMdiSubWindow()
        sub_window.setWindowTitle('Unterfenster')
        sub_window.setWidget(QTextEdit())
        self.mdi.addSubWindow(sub_window)
        sub_window.show()

    def close_active_subwindow(self):
        active_window = self.mdi.activeSubWindow()
        if active_window:
            active_window.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MDIExample()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec_())
