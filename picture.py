import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap, QPalette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a central widget and set it as the main window's central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create a label to hold the background image
        background_label = QLabel()
        layout.addWidget(background_label)

        # Load the background image using QPixmap
        pixmap = QPixmap(r"C:\Users\Admin\PyQt\fuji.jpg")  # Replace "background.jpg" with the path to your image
        background_label.setPixmap(pixmap)

        # Scale the label to fit the window size
        background_label.setScaledContents(True)

        # Set the label as the background widget
        self.setCentralWidget(background_label)

        # Set the window properties
        self.setWindowTitle("Background Image Example")
        self.setGeometry(100, 100, 800, 600)  # Set the window size

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
