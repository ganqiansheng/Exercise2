#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import  sys
from PyQt5.QtWidgets import *

class QLineEditEchoMode(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("文本输入框的回显模式")

        normalLineEdit=QLineEdit()
        noEchoLineEdit=QLineEdit()
        passwordLineEdit=QLineEdit()
        passwordOnEchoLineEdit=QLineEdit()

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordOnEchoLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordOnEchoLineEdit.setPlaceholderText("PasswordOnEcho")

        formLayout=QFormLayout()
        formLayout.addRow("Normal",normalLineEdit)
        formLayout.addRow("NoEcho",noEchoLineEdit)
        formLayout.addRow("Password",passwordLineEdit)
        formLayout.addRow("PasswordOnEcho",passwordOnEchoLineEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(QApplication.exec_())




