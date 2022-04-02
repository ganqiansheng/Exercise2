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
        self.setWindowTitle('Slider滑块控件演示')

        layout = QVBoxLayout()
        label=QLabel("滑块控件")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        slider=QSlider(Qt.Horizontal)
        slider.setRange(9,48)
        slider.setTickPosition(slider.TicksBelow)
        slider.setValue(18)
        layout.addWidget(slider)
        print(str(slider.maximum()))
        print(str(slider.minimum()))
        slider.valueChanged.connect(lambda:self.ValueChanged(label))
        slider.valueChanged.connect(self.SliderLeave)
        # spinBox.leaveEvent.connect(self.SpinBoxLeave)

        self.setLayout(layout)

    def SliderLeave(self):
        print('离开spinBox')
    def ValueChanged(self,objectLabel):
        slider=self.sender()
        label=objectLabel
        size=slider.value()
        label.setFont(QFont('Microsoft JhengHei Light',size))  #Microsoft JhengHei Light
        label.setText('滑块控件字号为：'+str(slider.value())  + '号字')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()

    sys.exit(QApplication.exec_())
