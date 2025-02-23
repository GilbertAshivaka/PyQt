import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QFormLayout,
    QLabel,
    QLineEdit, 
    QVBoxLayout
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt QWidget Demo ')
        self.setGeometry(100, 100, 800, 210)

        layout = QHBoxLayout(self)
        self.setLayout(layout)

        #person_pane
        person_pane = QWidget(self)
        form_layout = QFormLayout()
        person_pane.setLayout(form_layout)
        form_layout.addRow('First Name : ', QLineEdit(person_pane))
        form_layout.addRow('Last Name : ', QLineEdit(person_pane))
        form_layout.addRow('Date of Birth :', QLineEdit(person_pane))
        form_layout.addRow('Email Adress :', QLineEdit(person_pane))
        form_layout.addRow('Phone Number : ', QLineEdit(person_pane))

        layout.addWidget(person_pane)

        #adress_pane
        adress_pane = QWidget(self)
        form_layout = QFormLayout()
        adress_pane.setLayout(form_layout)
        form_layout.addRow('Street : ', QLineEdit(adress_pane))
        form_layout.addRow('City : ', QLineEdit(adress_pane))
        form_layout.addRow('State/Province : ', QLineEdit(adress_pane))
        form_layout.addRow('Zip Code : ', QLineEdit(adress_pane))
        form_layout.addRow('Country : ', QLineEdit(adress_pane))

        layout.addWidget(adress_pane)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

