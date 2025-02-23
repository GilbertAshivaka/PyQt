import sys
from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QPushButton, QGridLayout, QInputDialog
from PyQt6.QtGui import QIcon


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('My Wishlist')
        self.setWindowIcon(QIcon(r'C:\Users\Admin\PyQt\assets\icons8-wish-list-64.png'))
        self.setGeometry(100, 100, 320, 210)

        layout = QGridLayout(self)
        self.setLayout(layout)

        self.wish_list = QListWidget(self)
        self.wish_list.addItems([ 'Learn Python', 'Master PyQt'])
        
        layout.addWidget(self.wish_list, 0, 0, 4, 1)

        btn_add = QPushButton('Add')
        btn_add.clicked.connect(self.add)

        btn_insert = QPushButton('Insert')
        btn_insert.clicked.connect(self.insert)

        btn_remove = QPushButton('Remove')
        btn_remove.clicked.connect(self.remove)

        btn_clear = QPushButton('Clear')
        btn_clear.clicked.connect(self.clear)

        layout.addWidget(btn_add, 0, 1)
        layout.setRowStretch(0, 0)
        layout.addWidget(btn_insert, 1, 1)
        layout.setRowStretch(1, 0)
        layout.addWidget(btn_remove, 2, 1)
        layout.setRowStretch(2, 0)
        layout.addWidget(btn_clear, 3, 1)

        self.show()

    def add(self):
        text, ok = QInputDialog.getText(self, 'Add a new wish', 'New Wish: ')
        if ok and text:
            self.wish_list.addItem(text)

    def insert(self):
        text, ok = QInputDialog.getText(self, 'Add a new wish', 'New wish: ')
        if ok and text:
            current_row = self.wish_list.currentRow()
            current_row = current_row+1
            self.wish_list.insertItem(current_row, text)

    def remove(self):
        current_item = self.wish_list.currentItem()
        if current_item is not None:
            self.wish_list.takeItem(self.wish_list.row(current_item))
            del current_item
            

    def clear(self):
        self.wish_list.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
