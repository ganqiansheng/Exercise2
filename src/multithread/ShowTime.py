import sys,time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *


class ShowTime(QWidget):
    def __init__(self):
        super(ShowTime,self).__init__()

        self.setWindowTitle('时间控件演示案例')
        self.resize(300,200)

        layout=QGridLayout()
        self.label=QLabel('显示当前时间')
        self.buttonStart=QPushButton('开始')
        self.buttonEnd=QPushButton('结束')
        self.buttonEnd.setEnabled(False)

        self.buttonStart.clicked.connect(self.startTimer)
        self.buttonEnd.clicked.connect(self.endTimer)

        layout.addWidget(self.label,0,0,2,1)
        layout.addWidget(self.buttonStart,1,0)
        layout.addWidget(self.buttonEnd,1,1)

        self.setLayout(layout)

        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)

    def showtime(self):
        time=QDateTime.currentDateTime()
        timeDisplay=time.toString('yyyy-mm-dd hh:mm:ss')
        self.label.setText('当前时间：'+timeDisplay)

    def startTimer(self):
        self.timer.start(1000)
        self.buttonStart.setEnabled(False)
        self.buttonEnd.setEnabled(true)

    def endTimer(self):
        self.timer.stop()
        self.buttonStart.setEnabled(True)
        self.buttonEnd.setEnabled(False)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ScrollBar()
    main.show()

    sys.exit(app.exec_())
