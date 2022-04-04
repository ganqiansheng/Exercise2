

import sys

from PyQt5.QtCore import QMimeData
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class StatusBar(QMainWindow):
    def __init__(self):
        super(StatusBar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('状态栏演示案例')
        self.resize(600,400)

        bar=QMenuBar(self)
        file=bar.addMenu('文件')

        self.actionNew=QAction('新建',self)
        self.actionNew.setShortcut('ctrl+N')
        file.addAction(self.actionNew)


        self.actionOpen=QAction('打开',self)
        file.addAction(self.actionOpen)

        file.triggered.connect(self.ProcessTrigged)

        self.statusBar=QStatusBar()
        self.setStatusBar(self.statusBar)


    def ProcessTrigged(self,q):
        self.statusBar.showMessage(q.text()+'被点击',10000)











if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StatusBar()
    main.show()

    sys.exit(QApplication.exec_())
