import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QStatusBar, QToolBar
from PyQt6.QtGui import QIcon, QAction


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Awsome Editor')
        self.setWindowIcon(QIcon(r'C:\\Users\Admin\PyQt\assets\icons8-pencil-48.png'))
        self.setGeometry(100, 100, 500, 300)
        
        self.text_editor = QTextEdit(self)
        self.setCentralWidget(self.text_editor)

        #Settings Menu
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('&File')
        edit_menu = menu_bar.addMenu('&Edit')
        help_menu = menu_bar.addMenu('&Help')

        #Adding Action/ functionalities
        file_menu.addAction('New', lambda: self.text_editor.clear())
        file_menu.addAction('Open', lambda: print('Open'))
        file_menu.addAction('Exit', lambda: self.destroy())

        #Adding Actions to the Toolbar
        undo_action = QAction(QIcon(r'C:\\Users\Admin\PyQt\assets\icons8-undo-40.png'), 'Undo', self)
        undo_action.setShortcut('Ctrl+Z')
        undo_action.triggered.connect(self.text_editor.undo)
        edit_menu.addAction(undo_action)

        #Redo action 
        redo_action = QAction(QIcon(r'C:\\Users\Admin\PyQt\assets\icons8-redo-40.png'), 'Redo', self)
        redo_action.setShortcut('Ctrl+Y')
        redo_action.triggered.connect(self.text_editor.redo)
        edit_menu.addAction(redo_action)

        #Adding the toolbar
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)

        toolbar.addAction(undo_action)
        toolbar.addAction(redo_action)


        #set Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage('Awsome Editor V1.0')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())