import sys 
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QFormLayout,
    QLineEdit, QPushButton, QTableWidget,
    QTableWidgetItem,QToolBar, QMessageBox,
    QDockWidget, QSpinBox
)

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Employees')
        self.setWindowIcon(QIcon(r'C:\Users\Admin\PyQt\assets\icons8-user-group-female-skin-type-7-48.png'))
        self.setGeometry(100, 100, 600, 400)

        employees = [ 
            {'First Name':'John', 'Last Name': 'Muller', 'Age': 25},
            {'First Name': 'Jane', 'Last Name': 'Muller', 'Age': 22},
            {'First Name':'Alex', 'Last Name': 'Muller', 'Age': 22}
        ]

        self.table = QTableWidget(self)
        self.setCentralWidget(self.table)

        self.table.setColumnCount(3)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 50)

        self.table.setHorizontalHeaderLabels(employees[0].keys())
        self.table.setRowCount(len(employees))


        row = 0
        for e in employees:
            self.table.setItem(row, 0, QTableWidgetItem(e['First Name']))
            self.table.setItem(row, 1, QTableWidgetItem(e['Last Name']))
            self.table.setItem(row, 2, QTableWidgetItem(str(e['Age'])))
            row +=1



        dock = QDockWidget(self)
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)

        form = QWidget()
        layout = QFormLayout(form)
        form.setLayout(layout)

        self.first_name = QLineEdit(form)
        self.last_name = QLineEdit(form)
        self.age = QSpinBox(form, minimum=17, maximum=67)
        self.age.clear()
        
        btn_add = QPushButton('Add')
        btn_add.clicked.connect(self.add)

        layout.addRow('First Name:', self.first_name)
        layout.addRow('Last Name:', self.last_name)
        layout.addRow('Age:', self.age)
        layout.addRow(btn_add)

        toolbar = QToolBar('Main Toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        delete_action = QAction(QIcon(r'C:\Users\Admin\PyQt\assets\icons8-delete-48.png'), "&Delete", self)
        delete_action.triggered.connect(self.delete)
        delete_action.setShortcut('DELETE')
        toolbar.addAction(delete_action)

        dock.setWidget(form)

    def delete(self):
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        current_row = self.table.currentRow()
        if current_row <0:
            QMessageBox.warning(
                self,
                  'Warning',
                  'Please select an item to delete'
                    )
        button = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete the selected record',
                                        QMessageBox.StandardButton.Yes |
                                        QMessageBox.StandardButton.No )
        if button == QMessageBox.StandardButton.Yes:
            self.table.removeRow(current_row)

    def valid(self):
        first_name = self.first_name.text().strip()
        last_name = self.last_name.text().strip()

        if not first_name:
            QMessageBox.critical(self, 'Error', ' Please enter the first name')
            self.first_name.setFocus()
            return False
        
        if not last_name:
            QMessageBox.critical(self, 'Error', 'Please enter the last name')
            self.last_name.setFocus()
            return False
        
        try: 
            age = int(self.age.text().strip())
        except:
            ValueError
            QMessageBox.critical(self, 'Error', 'Enter a valid age')
            self.age.setFocus()
            return False
        
        if age < 18 or age >67:
            QMessageBox.critical(self, 'Error', 'A valid age is between 18 and 67')
            self.age.setFocus()
            return False
        
        return True
    
    def reset(self):
        self.first_name.clear()
        self.last_name.clear()
        self.age.clear()

    def add(self):
        if not self.valid():
            return
        
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(self.first_name.text().strip()))
        self.table.setItem(row, 1, QTableWidgetItem(self.last_name.text().strip()))
        self.table.setItem(row, 2, QTableWidgetItem(self.age.text().strip()))

        self.reset()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

            
