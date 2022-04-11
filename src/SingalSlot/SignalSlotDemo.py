import os
import sys
from PyQt5.QtCore import QUrl, QObject, pyqtSlot, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtGui import *

class SignalSlotDemo(QWidget):
    def __init__(self):
        super(SignalSlotDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Signal and Slot')
        self.resize(500,400)
        self.btn=QPushButton('我的按钮',self)
        self.btn.clicked.connect(self.onClick)

    def onClick(self):
        self.btn.setText('信号已经发出')
        self.btn.setStyleSheet('QPushButton(Max-width:200px;min-width:200px')



if __name__=='__main__':
    app=QApplication(sys.argv)
    main=SignalSlotDemo()
    main.show()

    sys.exit(app.exec_())




