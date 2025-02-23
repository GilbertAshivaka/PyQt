import sys
from PyQt6.QtWidgets import(
    QApplication,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QCompleter
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('LineEdit Widget')
        self.setGeometry(100, 100, 320, 210)

        search_box = QLineEdit(
            self,
            placeholderText = 'Enter a keyword to search...',
            clearButtonEnabled = True
        )

        password = QLineEdit(self, echoMode= QLineEdit.EchoMode.Password)

        common_fruits = QCompleter([
            'Apple',
            'Apricot',
            'Banana',
            'Carambola',
            'Olive',
            'Oranges',
            'Papaya',
            'Peach',
            'Pineapple',
            'Pomegranate',
            'Rambutan',
            'Ramphal',
            'Raspberries',
            'Rose apple',
            'Starfruit',
            'Strawberries',
            'Water apple',
        ])

        fruits = QLineEdit(self)
        fruits.setCompleter(common_fruits)



        layout = QVBoxLayout()
        layout.addWidget(search_box)
        layout.addWidget(password)
        layout.addWidget(fruits)
        self.setLayout(layout)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())