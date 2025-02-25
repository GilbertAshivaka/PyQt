import sys
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QTreeWidget, 
    QTreeWidgetItem,
    
)

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Tree widget')
        self.setGeometry(100, 100, 400, 200)
        
        tree = QTreeWidget(self)
        tree.setColumnCount(2)
        tree.setHeaderLabels(['Departmets', 'Employees'])

        departments = ['Sales', 'Marketing','Human Resource']
        employees = {
        'Sales':['John', 'Jane', 'Peter'],
        'Marketing': ['Alice', 'Bob'],
        'Human Resource':['Alex']
        }

        for department in departments:
            department_item = QTreeWidgetItem(tree)
            department_item.setText(0, department)
            for employee in employees[department]:
                employee_item = QTreeWidgetItem(tree)
                employee_item.setText(1, employee)

                department_item.addChild(employee_item)

        #place the tree widget on the maiinwindow
        self.setCentralWidget(tree)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())