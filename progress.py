import sys
from PyQt6.QtWidgets import  QApplication, QWidget, QHBoxLayout, QVBoxLayout, QProgressBar, QPushButton
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt Progress Widget ')
        

        layout = QVBoxLayout()
        self.setLayout(layout)

        hbox = QHBoxLayout()

        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)

        layout.addLayout(hbox)

        self.btn_progress = QPushButton('Progress', clicked =self.progress)
        self.btn_reset = QPushButton('Reset',clicked= self.reset)

        hbox.addStretch()
        hbox.addWidget(self.btn_progress)
        hbox.addWidget(self.btn_reset)
        hbox.addStretch()


        self.current_value = 0
        #layout.addLayout(hbox)
        self.show()
    
    def progress(self):
        if self.current_value <= self.progress_bar.maximum():
            self.current_value += 5
            self.progress_bar.setValue(self.current_value)

    def reset(self):
        self.current_value = 0
        self.progress_bar.reset()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())



