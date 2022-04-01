#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import  sys
from PyQt5.QtWidgets import *

class QlabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300,200)

        nameLabel=QLabel('&Name',self)
        nameLineText=QLineEdit(self)
        nameLabel.setBuddy(nameLineText)

        passwordLabel=QLabel('&password',self)
        passwordLineText=QLineEdit(self)
        passwordLabel.setBuddy(passwordLineText)

        buttonOK=QPushButton('确定(&ok)')
        buttonCancel=QPushButton('取消(&Cancel')

        Layout=QGridLayout()
        Layout.addWidget(nameLabel,0,0)
        Layout.addWidget(nameLineText,0,1,1,2)
        Layout.addWidget(passwordLabel,1,0)
        Layout.addWidget(passwordLineText,1,1,1,2)
        Layout.addWidget(buttonOK,2,1)
        Layout.addWidget(buttonCancel,2,2)

        self.setLayout(Layout)

        buttonOK.clicked.connect(self.buttonOKClick)
        buttonCancel.clicked.connect(self.buttonCancelClick)
    def buttonOKClick(self):
        print('buttonOK被点击')
    def buttonCancelClick(self):
        print('buttonCancel被点击')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QlabelBuddy()
    main.setWindowTitle('QLabel伙伴控件演示')
    main.show()

    sys.exit(QApplication.exec_())




