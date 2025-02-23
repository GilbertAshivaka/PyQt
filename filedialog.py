import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, 
    QFileDialog, 
    QPushButton,
    QGridLayout,
    QLabel,
    QListWidget
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

        self.file_list = QListWidget(self)

        label = QLabel('File:')

        layout.addWidget(label, 0,0)
        layout.addWidget(self.file_list)
        layout.addWidget(btn_file_browser)

        self.show()

    def open_file_dialog(self):
        dialog = QFileDialog(self)
        dialog.setDirectory(r'C:\Users\Admin\Downloads')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        #dialog.setFilter("Images (*.png *.jpg)")
        dialog.setViewMode(QFileDialog.ViewMode.Detail)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                self.file_list.addItems([str(Path(filename)) for filename in filenames])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindo()
    sys.exit(app.exec())
