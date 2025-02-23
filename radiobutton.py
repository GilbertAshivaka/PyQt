import sys

from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt Radio Button Widget')
        self.setGeometry(100, 100, 320, 210)

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('Please select a plartform')

        rb_android = QRadioButton('Android', self)
        rb_android.toggled.connect(self.update)

        rb_ios = QRadioButton('iOS', self)
        rb_ios.toggled.connect(self.update)

        rb_windows = QRadioButton('Windows', self)
        rb_windows.toggled.connect(self.update)

        self.result_label = QLabel('', self)

        layout.addWidget(label)
        layout.addWidget(rb_android)
        layout.addWidget(rb_ios)
        layout.addWidget(rb_windows)
        layout.addWidget(self.result_label)

        #Show the window
        self.show()

    
    def update(self):
        rb = self.sender()

        if rb.isChecked():
            self.result_label.setText(f'You selected {rb.text()}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())