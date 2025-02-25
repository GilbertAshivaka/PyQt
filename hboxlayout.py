import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
        self.setWindowTitle('Qt HboxLayout Widget')

        layout = QHBoxLayout()
        self.setLayout(layout)

        titles = ['Yes', 'No', 'Cancel']

        buttons = [QPushButton(title) for title in titles]
        for button in buttons:
            layout.addWidget(button)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())