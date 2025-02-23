from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QPoint, QRect, QPropertyAnimation, QEasingCurve, Qt, QEvent
from PyQt6 import QtGui
from PyQt6 import QtCore

class SlidingWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.menu_visible = False
        self.menu_width = 200
        self.main_window_width = 600

        self.init_ui()


    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.content_widget = QWidget()
        layout.addWidget(self.content_widget)

        self.menu_button = QPushButton("Menu")
        layout.addWidget(self.menu_button)

        self.menu_button.clicked.connect(self.toggle_menu)

        # Create the menu widget
        self.menu_widget = QWidget(self)
        self.menu_widget.setGeometry(QRect(-self.menu_width, 0, self.menu_width, self.height()))

        menu_layout = QVBoxLayout()
        self.menu_widget.setLayout(menu_layout)

        for i in range(1, 6):
            button = QPushButton(f"Option {i}")
            # button.setStyleSheet('border: solid 5px')
            menu_layout.addWidget(button)
        menu_layout.addStretch()

        self.animation = QPropertyAnimation(self.menu_widget, b"pos")
        self.animation.setDuration(800)
        easing_curve = QEasingCurve(QEasingCurve.Type.InOutBack)
        self.animation.setEasingCurve(easing_curve)

        # Signal to hide menu when clicked anywhere outside of it
        self.menu_widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.menu_widget.installEventFilter(self)
        self.content_widget.installEventFilter(self)

    def toggle_menu(self):
        if not self.menu_visible:
            self.menu_widget.move(0, 0)  # Move the menu to the left side of the screen
            self.animation.setStartValue(QPoint(-self.menu_width, 0))
            self.animation.setEndValue(QPoint(0, 0))
            self.animation.start()
        else:
            self.animation.setStartValue(QPoint(0, 0))
            self.animation.setEndValue(QPoint(-self.menu_width, 0))
            self.animation.start()

        self.menu_visible = not self.menu_visible

    def eventFilter(self, obj, event):
        print(type(event))
        # print(type(obj))
        if obj == self.centralWidget() and event.type() == QtCore.QEvent and self.menu_visible:
            self.toggle_menu()
        return super().eventFilter(obj, event)

    
    

if __name__ == "__main__":
    app = QApplication([])
    window = SlidingWindow()
    window.setWindowTitle("Sliding Window")
    window.setGeometry(100, 100, 600, 400)
    window.show()
    app.exec()
