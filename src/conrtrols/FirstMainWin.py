#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin,self).__init__()
        self.setWindowTitle('第一个主窗口应用')
        self.resize(400,300)
        self.status=self.statusBar()
        self.status.showMessage('只存在5秒种',5000)
if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/0.ICO'))
    main=FirstMainWin()

    main.show()

    sys.exit(app.exec_())