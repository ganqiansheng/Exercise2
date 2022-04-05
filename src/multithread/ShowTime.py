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

        self.layout=QGridLayout()
        self.label=QLabel('显示当前时间')
        self.buttonStart=QPushButton('开始')
        self.buttonEnd=QPushButton('结束')
        self.buttonEnd.setEnabled(False)

        self.buttonStart.clicked.connect(self.startTimer)
        self.buttonEnd.clicked.connect(self.endTimer)

        self.layout.addWidget(self.label,0,0,1,2)
        self.layout.addWidget(self.buttonStart,1,0)
        self.layout.addWidget(self.buttonEnd,1,1)

        self.setLayout(self.layout)

        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)

    def showTime(self):
        time=QDateTime.currentDateTime()
        timeDisplay=time.toString('yyyy-mm-dd hh:mm:ss dddd')
        self.label.setText('当前时间：'+timeDisplay)

    def startTimer(self):
        self.timer.start(1000)
        self.buttonStart.setEnabled(False)
        self.buttonEnd.setEnabled(True)

        self.label2=QLabel('如不停止计时器，程序在5秒后退出')
        self.layout.addWidget(self.label2,2,0,1,2)

        self.timer.singleShot(5000,self.quitApp)

    def endTimer(self):
        self.timer.stop()
        self.buttonStart.setEnabled(True)
        self.buttonEnd.setEnabled(False)

    def quitApp(self):
        app=QApplication.instance()
        app.quit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ShowTime()
    main.show()

    sys.exit(app.exec_())
