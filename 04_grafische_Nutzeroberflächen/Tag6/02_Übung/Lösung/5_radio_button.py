import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QLabel, QVBoxLayout, QWidget, QButtonGroup

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Erstelle ein zentrales Widget und ein Layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Erstelle eine Button-Gruppe
        button_group = QButtonGroup()

        # Erstelle Radiobuttons
        self.radio_button_1 = QRadioButton('Option 1', self)
        button_group.addButton(self.radio_button_1)
        self.radio_button_1.toggled.connect(self.update_label)
        layout.addWidget(self.radio_button_1)

        self.radio_button_2 = QRadioButton('Option 2', self)
        button_group.addButton(self.radio_button_2)
        self.radio_button_2.toggled.connect(self.update_label)
        layout.addWidget(self.radio_button_2)

        # Erstelle ein Label
        self.label = QLabel('Keine Option ausgewählt', self)
        layout.addWidget(self.label)

        self.setCentralWidget(central_widget)
        self.setWindowTitle('Radiobuttons und Label')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def update_label(self):
        if self.radio_button_1.isChecked():
            self.label.setText('Option 1 ist ausgewählt!')
        elif self.radio_button_2.isChecked():
            self.label.setText('Option 2 ist ausgewählt!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
