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

        self.diamond_label = QLabel()

        self.height = QLineEdit()
        self.height.setPlaceholderText('Enter diamond height')

        self.button = QPushButton('Show Diamond')
        self.button.clicked.connect(self.display_diamond)
        
        #place the widget on the wiindow 
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.height)
        layout.addWidget(self.button)
        layout.addWidget(self.diamond_label)
        
        self.setLayout(layout)

        layout.addStretch(10)

        #show the window
        self.show()
    
        
    
    def display_diamond(self):
        h = int(self.height.text())

        diamond = ""
        for i in range(h):
            diamond += " " * (h - i)
            diamond += "⭐" * (2 * i + 1)
            diamond += "\n"
        for i in range(h - 2, -1, -1):
            diamond += " " * (h - i)
            diamond += "⭐" * (2 * i + 1)
            diamond += "\n"

        self.diamond_label.setText(diamond)
        #♦

#create the main window
if __name__ =="__main__":
    app = QApplication(sys.argv)

    #create the main window 
    window = MainWindow()

    #set the event loop
    sys.exit(app.exec()) 