import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, 
    QFileDialog, 
    QPushButton,
    QGridLayout,
    QLabel,
    QListWidget,
    QLineEdit
    )

from pathlib import Path

class MainWindo(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt FileDialog Demo')
        self.setGeometry(100, 100, 320, 210)

        layout = QGridLayout(self)
        self.setLayout(layout)

        btn_file_browser = QPushButton('Browse')
        btn_file_browser.clicked.connect(self.open_file_dialog)

        self.file_name_edit = QLineEdit()

        layout.addWidget(QLabel('File : '), 0, 0)
        layout.addWidget(self.file_name_edit, 0, 1)
        layout.addWidget(btn_file_browser, 0, 2)


        self.show()

    def open_file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(
            self, 
            "Select a File",
            "C:\\Users\Admin\Downloads"

        )
        if filename:
            path = Path(filename)
            self.file_name_edit.setText(str(path))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindo()
    sys.exit(app.exec())
