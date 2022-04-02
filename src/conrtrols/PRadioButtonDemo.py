#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys,os
from PyQt5.QtWidgets import *


class QlabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 200)

        layout = QHBoxLayout()
        RadioButton1 = QRadioButton('单选按钮1')
        RadioButton1.setChecked(True)
        RadioButton1.toggled.connect(self.ButtonState)
        RadioButton1.setChecked(True)
        layout.addWidget(RadioButton1)

        RadioButton2=QRadioButton('单选按钮2')
        RadioButton2.setChecked(False)
        RadioButton2.toggled.connect(self.ButtonState)
        layout.addWidget(RadioButton2)

        self.setLayout(layout)

    def ButtonState(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print('< ' + radioButton.text() + ' >被选中')
        else:
            print('< ' + radioButton.text() + ' >未被选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QlabelBuddy()
    main.setWindowTitle('QRadioButton控件演示')
    main.show()

    sys.exit(QApplication.exec_())
