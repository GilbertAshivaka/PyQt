import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QSpinBox, QFormLayout
from PyQt6.QtCore import Qt 


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt SpinBox Widget')
        self.setGeometry(100, 100, 320, 210)

        layout = QFormLayout(self)
        self.setLayout(layout)

        amount = QSpinBox(minimum=1, maximum=100, value=20, prefix='$')
        amount.valueChanged.connect(self.update)

        label = QLabel('Enter the amount below:')
        self.result_label = QLabel(self)

        layout.addRow(label)
        layout.addRow('Amount:', amount)
        layout.addRow(self.result_label)

        

        self.show()
    

    def update(self, value):
        self.result_label.setText(f'Current amout: {value}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())