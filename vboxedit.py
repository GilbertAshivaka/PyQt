import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('QVBoxEdit Widget')
        self.setGeometry(100, 100, 320, 210)



        layout = QVBoxLayout()
        self.setLayout(layout)


        titles = ['Find next', 'Find All', 'Close']
        buttons = [ QPushButton(title) for title in titles]

        for button in buttons:
            layout.addWidget(button)
        
        layout.addStretch()


        ''''
        find_next_btn = QPushButton('Find next')
        find_all_btn = QPushButton('Find All')
        close_btn = QPushButton('Close')


        
        layout.addWidget(find_next_btn)
        layout.addWidget(find_all_btn)

        layout.addStretch()
        layout.addWidget(close_btn)
        '''
        label_1 = QLabel()
        label_1.setStyleSheet('QLabel{background-color: brown}')
        label_2 = QLabel()
        label_2.setStyleSheet('QLabel{background-color: mediumseagreen}')
        label_3 = QLabel()
        label_3.setStyleSheet('QLabel{background-color: orange}')

        layout.addWidget(label_1)
        layout.addWidget(label_2)
        layout.addWidget(label_3)

        layout.setStretchFactor(label_1, 1)
        layout.setStretchFactor(label_2, 2)
        layout.setStretchFactor(label_3, 3)

        '''
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 50, 100 )
        '''



        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())