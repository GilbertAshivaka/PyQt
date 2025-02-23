import sys 
from PyQt6.QtWidgets import QApplication, QTabWidget, QLineEdit, QFormLayout, QGridLayout,QWidget, QDateEdit, QPushButton
 
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt Tab Widget')
        self.setGeometry(100, 100, 320, 210)
        
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        tab = QTabWidget(self)


        #personal information
        personal_page = QWidget(self)
        layout = QFormLayout()
        personal_page.setLayout(layout)
        layout.addRow('First Name : ', QLineEdit(personal_page))
        layout.addRow('Last Name : ', QLineEdit(personal_page))
        layout.addRow('DOB: ', QDateEdit(personal_page, calendarPopup=True))

        #contact info
        contact_page = QWidget(self)
        layout = QFormLayout()
        contact_page.setLayout(layout)
        layout.addRow('Phone Number : ', QLineEdit(contact_page))
        layout.addRow('Email Adress :', QLineEdit(contact_page))

        #add the pages to the tab
        tab.addTab(personal_page, 'Personal Info')
        tab.addTab(contact_page, 'Contact Info')


        main_layout.addWidget(tab, 0, 0, 2, 1)

        main_layout.addWidget(QPushButton('Save'), 2, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(QPushButton('Cancel'), 2, 0, alignment= Qt.AlignmentFlag.AlignRight)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
