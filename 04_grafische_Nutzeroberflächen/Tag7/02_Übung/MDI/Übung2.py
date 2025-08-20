import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit, QLabel)


class MDIExample(QMainWindow):
    def __init__(self):
        super().__init__()

        # MDI-Bereich erstellen
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.setWindowTitle("MDI-Übung2")
        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('Datei')
        new_action = file_menu.addAction('Neu Text Editor')
        new_action.triggered.connect(self.create_document)
        new_action = file_menu.addAction('Neu Label')
        new_action.triggered.connect(self.create_label)

    def create_document(self):
        sub_window = QMdiSubWindow()
        sub_window.setWindowTitle('Text editor')
        sub_window.setWidget(QTextEdit())
        self.mdi.addSubWindow(sub_window)
        sub_window.show()

    def create_label(self):
        sub_window = QMdiSubWindow()
        sub_window.setWindowTitle('label')
        sub_window.setWidget(QLabel('Hallo World!'))
        sub_window.setGeometry('100x50')
        self.mdi.addSubWindow(sub_window)
        sub_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MDIExample()
    window.resize(600, 500)
    window.show()
    sys.exit(app.exec_())
