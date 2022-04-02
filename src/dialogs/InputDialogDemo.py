#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class QInputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('对话框演示')
        self.resize(400,200)

        layout=QFormLayout()
        self.button1=QPushButton('获取表单输入项')
        self.button2=QPushButton('获取文本输入项')
        self.button3=QPushButton('获取数字输入项')

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setPlaceholderText('获取表单输入项')
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setPlaceholderText('获取文本输入项')
        self.lineEdit3 = QLineEdit()
        self.lineEdit3.setPlaceholderText('获取数字输入项')

        layout.addRow(self.button1,self.lineEdit1)
        layout.addRow(self.button2,self.lineEdit2)
        layout.addRow(self.button3,self.lineEdit3)

        self.button1.clicked.connect(self.getItems)
        self.button2.clicked.connect(self.getText)
        self.button3.clicked.connect(self.getInt)

        self.setLayout(layout)

    def getItems(self):
        items=['Python','C++','C#','Ruby','Java']
        item,OK=QInputDialog.getItem(self,'获取表单输入项','请选择编程语言',items)
        if OK and item:
            self.lineEdit1.setText(item)
    def getText(self):
        text,OK=QInputDialog.getText(self,'获取文本输入项','请输入文本')
        if OK and text:
            self.lineEdit2.setText(text)
    def getInt(self):
        num,OK=QInputDialog.getInt(self,'获取数字输入项','请输入数字')
        if OK and num:
            self.lineEdit3.setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()

    sys.exit(QApplication.exec_())
