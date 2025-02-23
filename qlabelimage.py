import sys
from PyQt6.QtWidgets import QApplication,QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #set window title
        self.setWindowTitle("PyQt QLabel Widget")
        self.setGeometry(100, 100, 100, 100)

        #create the label instance 
        label = QLabel()
        pixmap = QPixmap("fuji.jpg")
        label.setPixmap(pixmap)

        #place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        

        #show the main window 
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)


    #create the main window
    window = MainWindow()

    #start the event loop
    sys.exit(app.exec())