#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class QFontDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('字体对话框演示')
        self.resize(300,200)

        layout=QVBoxLayout()
        self.button=QPushButton('设置字体')
        self.button.clicked.connect(self.FontSet)
        self.label=QLabel("hello,这是测试字体显示文字")

        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def FontSet(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.label.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.show()

    sys.exit(QApplication.exec_())
