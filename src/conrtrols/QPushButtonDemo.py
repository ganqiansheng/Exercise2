#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import  sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton按钮功能演示')
        self.resize(400,300)

        vBoxLayout=QVBoxLayout()

        #按钮1
        button1=QPushButton('第一个按钮')
        button1.setCheckable(True)
        button1.toggle()
        button1.clicked.connect(lambda:self.whichButton(button1))
        button1.clicked.connect(lambda:self.buttonStatus(button1))
        vBoxLayout.addWidget(button1)

        #按钮2
        button2=QPushButton('图像按钮')
        button2.setIcon(QIcon(QPixmap('.\\images\\png\\SolutionCover.png')))
        vBoxLayout.addWidget(button2)

        # 按钮3
        button3=QPushButton('不可用的按钮')
        button3.setEnabled(False)
        vBoxLayout.addWidget(button3)

        # 按钮4
        button4=QPushButton('&MyButton')
        button4.setDefault(True)
        button4.clicked.connect(lambda:self.whichButton(button4))
        vBoxLayout.addWidget(button4)

        self.setLayout(vBoxLayout)

    def whichButton(self,btn):
        print('被单击的按钮是：<'+btn.text()+'>')
        print(str(time.strftime("%Y-%m-%d %X",time.localtime())))
    def buttonStatus(self,btn):
        if btn.isChecked():
            print('按钮<'+btn.text()+'>被选中')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.setWindowTitle('用栅格布局组合多个命令按钮')
    main.show()

    sys.exit(QApplication.exec_())

