import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QFormLayout, QDateEdit

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt DateEdit Widget')
        self.setGeometry(100, 100, 320, 210)

        layout = QFormLayout(self)
        self.setLayout(layout)

        self.date_edit = QDateEdit(self)
        self.date_edit.editingFinished.connect(self.update)

        self.date_label = QLabel(self)

        layout.addRow('Date:', self.date_edit)
        layout.addRow(self.date_label)

        self.show()

    def update(self):
        value = self.date_edit.date()
        self.date_label.setText(str(value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())