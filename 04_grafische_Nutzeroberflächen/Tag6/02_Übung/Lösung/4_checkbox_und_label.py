import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel, QVBoxLayout, QWidget

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Erstelle ein zentrales Widget und ein Layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Erstelle eine Checkbox
        self.checkbox = QCheckBox('Aktiviere mich', self)
        self.checkbox.stateChanged.connect(self.update_label)
        layout.addWidget(self.checkbox)

        # Erstelle ein Label
        self.label = QLabel('Checkbox ist nicht ausgewählt!', self)
        layout.addWidget(self.label)

        self.setCentralWidget(central_widget)
        self.setWindowTitle('Checkbox und Label')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def update_label(self):
        if self.checkbox.isChecked():
            self.label.setText('Checkbox ist ausgewählt !')
        else:
            self.label.setText('Checkbox ist nicht ausgewählt !')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
