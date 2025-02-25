import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QVBoxLayout, QProgressBar
from PyQt6.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
import time 

class Worker(QObject):
    progress = Signal(int)
    completed = Signal(int)

    @Slot(int)
    def do_work(self, n):
        for i in range(1, n+1):
            time.sleep(1)
            self.progress.emit(i)

        self.completed.emit(i)


class MainWindow(QMainWindow):
    work_requested = Signal(int)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('QThreads Demo')
        # self.setGeometry(100, 100, 320, 210)
        

        self.widget = QWidget()
        layout = QVBoxLayout()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)

        self.btn_start = QPushButton('Start', clicked=self.start)

        layout.addWidget(self.progress_bar)
        layout.addWidget(self.btn_start)

        self.worker = Worker()
        self.worker_thread = QThread()

        self.worker.progress.connect(self.update_progress)
        self.worker.completed.connect(self.complete)

        self.work_requested.connect(self.worker.do_work) 

        #move to the worker thread
        self.worker.moveToThread(self.worker_thread)

        self.worker_thread.start()

        self.show()



    def start(self):
        self.btn_start.setEnabled(False)
        n = 5
        self.progress_bar.setMaximum(n)
        self.work_requested.emit(n)
    
    def update_progress(self, v):
        self.progress_bar.setValue(v)

    def complete(self, v):
        self.progress_bar.setValue(v)
        self.btn_start.setEnabled(True)


if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())