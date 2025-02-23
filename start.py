import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)


        #set the window title
        self.setWindowTitle("Hello World")

        #show window
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    #create the mainwindow
    window = MainWindow()

    #start the event loop
    sys.exit(app.exec())
