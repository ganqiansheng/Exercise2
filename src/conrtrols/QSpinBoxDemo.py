#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class QSpinBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 50)
        self.setWindowTitle('SpinBox计时器控件演示')

        layout = QVBoxLayout()
        label=QLabel("计时器当前值")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        spinBox=QSpinBox()
        spinBox.setRange(1,99999)
        layout.addWidget(spinBox)
        spinBox.valueChanged.connect(lambda:self.ValueChanged(label))
        spinBox.valueChanged.connect(self.SpinBoxLeave)
        # spinBox.leaveEvent.connect(self.SpinBoxLeave)

        self.setLayout(layout)

    def SpinBoxLeave(self):
        print('离开spinBox')
    def ValueChanged(self,objectLabel):
        spinBox=self.sender()
        label=objectLabel
        label.setText('计时器当前值:'+str(spinBox.value()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()

    sys.exit(QApplication.exec_())
