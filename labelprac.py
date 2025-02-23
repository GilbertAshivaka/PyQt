import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt6.QtGui import QFont


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt Label Widget")
        self.setGeometry(100, 100, 320, 210)

        #set a QLabel widget
        self.label = QLabel('This prints a diamond shape')


        #place the widget on the wiindow 
        layout = QVBoxLayout()
        layout.addWidget(self.label)
       
        
        self.setLayout(layout)

        #show the window
        self.show()


if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec()) 