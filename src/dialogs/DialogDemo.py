#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class QDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('对话框演示')
        self.resize(300,200)

        button=QPushButton(self)
        button.move(50,50)
        button.setText('弹出对话框')
        button.clicked.connect(self.ShowDialog)

    def ShowDialog(self):
        print('弹出对话框')
        dialog=QDialog()
        button=QPushButton('确定',dialog)
        button.clicked.connect(dialog.close)
        dialog.resize(300,200)
        button.move(50,50)
        dialog.move(self.frameGeometry().x()+50,self.frameGeometry().y()+50)
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.setWindowTitle('对话框')
        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()

    sys.exit(QApplication.exec_())
