import sys

from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QGridLayout, QPushButton
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt Checkbox Widget')
        self.setGeometry(100, 100, 320, 210)

        layout = QGridLayout()
        self.setLayout(layout)

        self.checkbox = QCheckBox('I agree', self)
        #checkbox.stateChanged.connect(self.on_state_changed)
        
        #A tristate checkbox
        self.go_on = QCheckBox('Continue', self)
        self.go_on.setTristate(True)

        check_button = QPushButton('Check', self)
        check_button.clicked.connect(self.check)

        uncheck_button = QPushButton('Uncheck', self)
        uncheck_button.clicked.connect(self.uncheck)

        layout.addWidget(self.checkbox, 0, 0,  alignment=Qt.AlignmentFlag.AlignLeft )
        layout.addWidget(self.go_on, 0, 1)
        layout.addWidget(check_button, 1, 0)
        layout.addWidget(uncheck_button, 1, 1)

        self.show()

    '''
    def on_state_changed(self, value):
        state = Qt.CheckState(value)
        if state == Qt.CheckState.Checked:
            print('Checked')
        elif state == Qt.CheckState.Unchecked:
            print('Unchecked')
    '''   

    def check(self):
        self.checkbox.setChecked(True)
    

    def uncheck(self):
        self.checkbox.setChecked(False)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())