import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtGui import QFont


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt Label Widget")
        self.setGeometry(100, 100, 320, 210)

        self.label = QLabel('This prints a diamond in the shell')

        self.button = QPushButton('Show Diamond')
        self.button.clicked.connect(self.diamond)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        layout.addStretch(10)

        self.show()

    def diamond(self):
        h = eval(input("How many asterisks high do you want the diamond to be? "))

        diamond_pattern = ''
        for i in range(h):
            diamond_pattern += " " * (h - i) + "♦" * (2 * i - 1) + '\n'
        for i in range(h - 2, -1, -1):
            diamond_pattern += " " * (h - i) + "♦" * (2 * i - 1) + '\n'

        self.label.setText(diamond_pattern)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
