import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton,QGridLayout
from PyQt6.QtCore import Qt 
from pathlib import Path as path

class Mainwindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Login Form')
        self.setGeometry(100, 100, 320, 210)


        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel('Username:'), 0, 0)
        layout.addWidget(QLineEdit(), 0, 1)

        layout.addWidget(QLabel('Password:'), 1, 0)
        layout.addWidget(QLineEdit(echoMode= QLineEdit.EchoMode.Password), 1, 1)

        layout.addWidget(QPushButton('Login'), 2, 1, alignment=Qt.AlignmentFlag.AlignRight)

        layout.rowStretch(0)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mainwindow()
    app.setStyleSheet(path("login.qss").read_text())
    sys.exit(app.exec())