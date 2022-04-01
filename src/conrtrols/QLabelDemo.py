#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import  sys
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout
from PyQt5.QtGui import QPalette,QPixmap
from PyQt5.QtCore import Qt

class QlabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(100,100,1000,600)
        label1=QLabel(self)
        label2=QLabel(self)
        label3=QLabel(self)
        label4=QLabel(self)

        palette=QPalette()

        palette.setColor(QPalette.Window,Qt.blue)

        label1.setText("<font color=yellow>这是一个文本标签</font>")
        label1.setAutoFillBackground(True)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        palette.setColor(QPalette.Window,Qt.gray)
        label2.setAutoFillBackground(True)
        label2.setPalette(palette)
        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        label3.setPixmap(QPixmap('.\\images\\PNG\\SolutionCover.png'))
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('<font color=red size=20>这是一个图片标签<font>')

        palette.setColor(QPalette.Window, Qt.darkGray)
        label4.setAutoFillBackground(True)
        label4.setPalette(palette)
        label4.setOpenExternalLinks(True)
        label4.setText("<a href='http://www.baidu.com'>这是一个链接，直接打开百度首页</a>")
        label4.setAlignment(Qt.AlignCenter)
        label4.setToolTip('这是一个超链接')

        layout=QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        self.setLayout(layout)
        self.setWindowTitle('标签控件演示')

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkActived)

        # self.widgetbutton.clicked.connect(self.onClickwidgetButton)

    def linkHovered(self):
        print('当鼠标滑过标签时触发事件')
    def linkActived(self):
        print('当鼠标单击标签时触发事件')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QlabelDemo()
    main.setWindowTitle('用栅格布局组合多个命令按钮')
    main.show()

    sys.exit(QApplication.exec_())
