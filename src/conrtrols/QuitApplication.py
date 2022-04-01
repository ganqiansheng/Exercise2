#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import sys

import self as self
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon


class QuitApplication(QMainWindow):
    def __init__(self, parent=None):
        super(QuitApplication, self).__init__(parent)
        self.resize(400, 300)
        self.setWindowTitle('退出应用程序')
        self.status = self.statusBar()
        self.status.showMessage('这是一个退出应用程序的应用，此消息在此停留10秒钟', 10000)

        self.button1 = QPushButton('退出应用程序', self)
        self.button1.clicked.connect(self.onClickButton)

        # self.button1 = QPushButton('按键1',self)
        # self.button1.clicked.connect(self.onClickButton)


        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onClickButton(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    print(os.getcwd() + '\\images\\telephone.ICO')
    app.setWindowIcon(QIcon(os.getcwd() + '\\images\\telephone.ico'))
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())
