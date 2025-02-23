import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QProgressBar, QListWidget
from PyQt6.QtCore import QRunnable, QObject, QThreadPool, pyqtSignal as Signal, pyqtSlot as Slot
import time 


class Signals(QObject):
    started = Signal(int)
    completed = Signal(int)


class Worker(QRunnable):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.signals = Signals()

    @Slot()
    def run(self):
        self.signals.started.emit(self.n)
        time.sleep(self.n*1.1)
        self.signals.completed.emit(self.n)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.setWindowTitle('Qthreadpool Demo')
        
        self.job_count = 10
        self.completed_jobs = []

        self.widget = QWidget()
        self.widget.setLayout(QGridLayout())
        self.setCentralWidget(self.widget)

        self.btn_start = QPushButton('Start', clicked= self.start_jobs)
        self.progress_bar = QProgressBar(minimum=0, maximum=self.job_count)
        self.list = QListWidget()

        self.widget.layout().addWidget(self.list, 0, 0, 1, 2)
        self.widget.layout().addWidget(self.progress_bar, 1, 0)
        self.widget.layout().addWidget(self.btn_start, 1, 1)

        self.show()



    def start_jobs(self):
        self.restart()
        pool = QThreadPool.globalInstance()

        for i in range(1, self.job_count+1):
            worker = Worker(i)
            worker.signals.completed.connect(self.complete)
            worker.signals.started.connect(self.start)
            pool.start(worker)

    
    def restart(self):
        self.list.clear()
        self.progress_bar.setValue(0)
        self.completed_jobs = []
        self.btn_start.setEnabled(False)

    def start(self, n):
        self.list.addItem(f'Job #{n} started...')

    def complete(self, n):
        self.list.addItem(f'Job #{n} completed')
        self.completed_jobs.append(n)
        self.progress_bar.setValue(len(self.completed_jobs))

        if len(self.completed_jobs) == self.job_count:
            self.btn_start.setEnabled(True)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
        