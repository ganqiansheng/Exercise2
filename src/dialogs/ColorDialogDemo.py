#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class QColorDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('字体对话框演示')
        self.resize(300,200)

        layout=QVBoxLayout()
        self.button=QPushButton('设置字体')
        self.button.clicked.connect(self.ColorSet)
        self.button2=QPushButton('设置背景颜色')
        self.button2.clicked.connect(self.BackColorSet)
        self.label=QLabel("hello,这是测试颜色显示文字")


        layout.addWidget(self.button)
        layout.addWidget(self.button2)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def ColorSet(self):
        color=QColorDialog.getColor()
        palette = QPalette()
        palette.setColor(QPalette.WindowText,color)
        self.label.setPalette(palette)

    def BackColorSet(self):
        color=QColorDialog.getColor()
        palette = QPalette()
        palette.setColor(QPalette.Window,color)
        self.label.setAutoFillBackground(True)
        self.label.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()

    sys.exit(QApplication.exec_())
