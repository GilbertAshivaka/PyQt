import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTimeEdit, QFormLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.setWindowTitle('Qt Time Widget')
        self.setGeometry(100, 100, 320, 210)

        layout = QFormLayout(self)
        self.setLayout(layout)

        self.time_edit = QTimeEdit(self)
        self.time_edit.editingFinished.connect(self.update)

        self.time_label = QLabel('', self)

        layout.addRow('Time:', self.time_edit)
        layout.addRow(self.time_label)


        self.show()

    def update(self):
        value = self.time_edit.time()
        self.time_label.setText(str(value.toPyTime()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())