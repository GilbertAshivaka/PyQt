import sys
import typing
from PyQt6 import QtCore 
from PyQt6.QtWidgets import(
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
    )

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #set the window title
        self.setWindowTitle("Qt signals and slots")

        #create a button and connect it's clicked signal to a function
        button = QPushButton("Click me")
        button.clicked.connect(self.button_clicked)

        #set widgets for signals that send data
        label = QLabel()
        line_edit = QLineEdit()
        line_edit.textChanged.connect(label.setText)


        #set the layout using the vertical box layout

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(button)
        layout.addWidget(label)
        layout.addWidget(line_edit)

        self.setLayout(layout)

        self.show()

    #define a function for what the button does 
    def button_clicked(self):
        print("Clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    #create a window and show it
    window = MainWindow()

    #start the event loop
    sys.exit(app.exec())

