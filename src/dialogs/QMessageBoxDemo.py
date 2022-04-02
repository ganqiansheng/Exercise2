#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class QDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('对话框演示')
        self.resize(300,400)

        layout=QVBoxLayout()
        self.button1=QPushButton('显示关于对话框')
        self.button2=QPushButton('显示消息对话框')
        self.button3=QPushButton('显示警告对话框')
        self.button4=QPushButton('显示错误对话框')
        self.button5=QPushButton('显示提问对话框')

        self.button1.clicked.connect(self.ShowDialog)
        self.button2.clicked.connect(self.ShowDialog)
        self.button3.clicked.connect(self.ShowDialog)
        self.button4.clicked.connect(self.ShowDialog)
        self.button5.clicked.connect(self.ShowDialog)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)

        self.setLayout(layout)

    def ShowDialog(self):
        sender=self.sender()
        if sender==self.button1:
            reply=QMessageBox.about(self,'关于','这是一个关于对话框')
            print(reply)
        elif sender == self.button2:
            QMessageBox.information(self, '消息', '这是一个消息对话框', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                    QMessageBox.Yes)
        elif sender==self.button3:
            QMessageBox.warning(self,'警告','这是一个警告对话框',QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel,QMessageBox.Yes)
        elif sender==self.button4:
            QMessageBox.critical(self,'错误','这是一个错误对话框',QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel,QMessageBox.Yes)
        elif sender==self.button5:
            QMessageBox.question(self,'提问','这是一个提问对话框',QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel,QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()

    sys.exit(QApplication.exec_())
