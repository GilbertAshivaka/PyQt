import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QInputDialog, QPushButton


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        layout = QVBoxLayout(self)
        self.setLayout(layout)

        btn_title = QPushButton('Set Window Title')
        btn_title.clicked.connect(self.set_title)

        layout.addWidget(btn_title)

        self.show()

    def set_title(self):
        title, ok = QInputDialog.getText(self, 'Title Setting', 'Title:')
        if ok and title:
            self.setWindowTitle(title)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())