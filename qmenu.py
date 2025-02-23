import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QToolBar, QMessageBox, QFileDialog
from PyQt6.QtGui import QAction, QIcon
from pathlib import Path


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowIcon(QIcon(r'C:\Users\Admin\PyQt\assets\icons8-pencil-48.png'))
        self.setGeometry(100, 100, 500, 300)

        self.title = 'Awsome Editor'
        self.filters = 'Text files (*.txt)'

        self.set_title()

        self.path = None

        self.text_editor = QTextEdit()

        container = QWidget(self)
        container.setLayout(QVBoxLayout())
        container.layout().addWidget(self.text_editor)
        self.setCentralWidget(container)
        container.setContentsMargins(5, 5, 5, 5)

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('&File')
        edit_menu = menu_bar.addMenu('&Edit')
        help_menu = menu_bar.addMenu('&Help')


        #Adding new action to the window 
        new_action = QAction(QIcon(r'C:\Users\Admin\PyQt\assets\icons8-new-file-48.png'), '&New', self)
        new_action.setStatusTip('Create new document')
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.new_document)
        file_menu.addAction(new_action)

        open_action = QAction(QIcon(r'C:\Users\Admin\PyQt\assets\icons8-open-document-48.png'), '&Open...', self)
        open_action.setStatusTip('Open Existing document')
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_document)
        file_menu.addAction(open_action)

        save_action = QAction(QIcon(r'C:\Users\Admin\PyQt\assets\icons8-save-48.png'), '&Save', self)
        save_action.setStatusTip('Save document')
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_document)
        file_menu.addAction(save_action)

        file_menu.addSeparator()

        #Exit action 
        exit_action = QAction(QIcon(r'C:\Users\Admin\PyQt\assets\icons8-logout-48.png'), '&Exit', self)
        exit_action.setStatusTip('Exit the program')
        exit_action.setShortcut('Alt+F4')
        exit_action.triggered.connect(self.quit)
        file_menu.addAction(exit_action)


        #Edit menu
        undo_action = QAction(QIcon(r'C:\Users\Admin\PyQt\assets\icons8-undo-40.png'), '&Undo', self)
        undo_action.setShortcut('Ctrl+Z')
        undo_action.setStatusTip('Go to previous action')
        undo_action.triggered.connect(self.text_editor.undo)
        edit_menu.addAction(undo_action)


        redo_action = QAction(QIcon(r'C:\Users\Admin\PyQt\assets\icons8-redo-40.png'), '&Redo', self)
        redo_action.setShortcut('Ctrl+Y')
        redo_action.setStatusTip('Return to the undone action')
        redo_action.triggered.connect(self.text_editor.redo)
        edit_menu.addAction(redo_action)

        about_action = QAction(QIcon(r'C:\Users\Admin\PyQt\assets\icons8-info-48.png'), '&About', self)
        about_action.setShortcut('F1')
        about_action.setStatusTip('About')
        help_menu.addAction(about_action)


        self.status_bar = self.statusBar()
        self.show()

    def set_title(self, filename=None):
        title = f"{filename if filename else 'Untitled'}- {self.title}"
        self.setWindowTitle(title)

    
    def confirm_save(self):
        if not self.text_editor.document().isModified():
            return True 
        
        message = f"Do you want to save changes to {self.path if self.path else 'Untitled'}?"
        MsgBoxBtn = QMessageBox.StandardButton
        MsgBoxBtn = MsgBoxBtn.Save | MsgBoxBtn.Discard | MsgBoxBtn.Cancel

        button = QMessageBox.question(
            self,
            self.title,
            message,
            buttons=MsgBoxBtn
        )

        if button == MsgBoxBtn.Cancel:
            return False
        
        if button == MsgBoxBtn.Save:
            self.save_documen()
        
        return True
    
    def new_document(self):
        if self.confirm_save():
            self.text_editor.clear()
            self.set_title()

    def save_document(self):
        if (self.path):
            return self.path.write_text(self.text_editor.toPlainText())
        
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File', filter=self.filters)

        if not filename:
            return
        
        self.path = Path(filename)
        self.path.write_text(self.text_editor.toPlainText())
        self.set_title()

    def open_document(self):
        filename, _ = QFileDialog.getOpenFileName(self, filter=self.filters)

        if filename:
            self.path = Path(filename)
            self.text_editor.setText(self.path.read_text())
            self.set_title(filename)

    def quit(self):
        self.confirm_save()
        self.destroy


if __name__ == '__main__':
    try:
        import ctypes
        myappid = 'mycompany.myproduct.subproduct.version'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    finally:
        app = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(app.exec())