import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('QPushbutton Widget')
        self.setGeometry(100, 100, 320, 210)

        button = QPushButton('Click here')
        button.clicked.connect(self.something)

        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)

        self.show()
    
    def something(self):
        print('I am getting better at this.')




if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())