import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt 

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt Combobox Widget')
        self.setGeometry(100, 100, 320, 210)

        layout = QVBoxLayout()
        self.setLayout(layout)

        cb_label = QLabel('Please Select Label', self)

        self.platform = QComboBox(self)
        self.platform.addItem('Android')
        self.platform.addItem('iOS')
        self.platform.addItem('Windows')

        self.platform.activated.connect(self.update)

        self.result_label = QLabel('')

        layout.addWidget(cb_label)
        layout.addWidget(self.platform)
        layout.addWidget(self.result_label)

        self.show()

    def update(self):
        self.result_label.setText(f'You selected {self.platform.currentText()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())