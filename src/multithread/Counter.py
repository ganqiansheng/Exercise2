import sys,time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

sec = 0

class WorkTread(QThread):
    timer = pyqtSignal()
    end = pyqtSignal()
    def run(self):
        while True:
            self.sleep(1)
            if sec == 20:
                self.end.emit()
                break
            self.timer.emit()

class Counter(QWidget):
    def __init__(self):
        super(Counter,self).__init__()

        self.setWindowTitle('使用线程类(QThread)演示案例')
        self.resize(300,200)

        layout=QVBoxLayout()
        self.lcdNumber =QLCDNumber()
        self.button=QPushButton('开始计数')

        self.workThread=WorkTread()

        self.workThread.timer.connect(self.countTime)
        self.workThread.end.connect(self.end)

        self.button.clicked.connect(self.work)

        layout.addWidget(self.lcdNumber)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def countTime(self):
        global sec
        sec +=1
        self.lcdNumber.display(sec)

    def end(self):
        QMessageBox.information(self,'计数器','计数结束',QMessageBox.Ok)

    def work(self):
        global sec
        sec=0
        self.workThread.start()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Counter()
    main.show()

    sys.exit(app.exec_())
