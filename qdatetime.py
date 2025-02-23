import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QDateTimeEdit, QFormLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt TimeEdit Widget')
        self.setGeometry(100, 100, 320, 210)

        layout = QFormLayout(self)
        self.setLayout(layout)

        self.date_time = QDateTimeEdit(self, calendarPopup=True)
        self.date_time.timeChanged.connect(self.update)

        self.result_label = QLabel('', self)

        layout.addRow('Date and Time:', self.date_time)
        layout.addRow(self.result_label)

        self.show()

    def update(self):
        value = self.date_time.dateTime()
        self.result_label.setText(str(value.toPyDateTime()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())