import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 320, 210)
        self.setWindowIcon(QIcon(r'C:\Users\Admin\PyQt\assets\icons8-lock-48.png'))

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        heading = QLabel('Welcome back')
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        heading.setObjectName('heading')

        subheading = QLabel('Please enter your email and password to login')
        subheading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subheading.setObjectName('subheading')

        email = QLineEdit(self)
        email.setPlaceholderText('Enter your email')

        password = QLineEdit(self)
        password.setEchoMode(QLineEdit.EchoMode.Password)
        password.setPlaceholderText('Enter your password')

        btn_login = QPushButton('Login')

        layout.addStretch()
        layout.addWidget(heading)
        layout.addWidget(subheading)
        layout.addWidget(QLabel('Email:'))
        layout.addWidget(email)
        layout.addWidget(QLabel('Password:'))
        layout.addWidget(password)
        layout.addWidget(btn_login)
        layout.addStretch()

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('login.qss').read_text())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



        