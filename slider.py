import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QFormLayout, QSlider
from PyQt6.QtCore import Qt 


class Mainwindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.setWindowTitle('Qt Slider Widget')
        self.setGeometry(100, 100, 320, 210)

        layout = QFormLayout(self)
        self.setLayout(layout)

        slider = QSlider(Qt.Orientation.Horizontal, self)
        slider.setRange(0, 100)
        slider.setValue(50)
        slider.setSingleStep(1)
        slider.setPageStep(10)
        slider.setTickPosition(QSlider.TickPosition.NoTicks)

        slider.valueChanged.connect(self.update)

        self.result_label = QLabel(self)

        layout.addRow(slider)
        layout.addRow(self.result_label)

        self.show()


    def update(self, value):
        self.result_label.setText(f'Current value: {value}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mainwindow()
    sys.exit(app.exec())

    
