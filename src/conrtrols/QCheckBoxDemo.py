#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class QCheckBoxDemo(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('复选框控件演示')
        self.resize(300, 200)

        layout = QHBoxLayout()

        self.checkBox1=QCheckBox('复选按钮1')
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(self.StateChange)
        layout.addWidget(self.checkBox1)

        self.checkBox2 = QCheckBox('复选按钮1')
        self.checkBox2.stateChanged.connect(self.StateChange)
        layout.addWidget(self.checkBox2)

        self.checkBox3 = QCheckBox('复选按钮1')
        self.checkBox3.setTristate()
        self.checkBox3.setChecked(Qt.PartiallyChecked)
        self.checkBox3.stateChanged.connect(self.StateChange)
        layout.addWidget(self.checkBox3)

        self.setLayout(layout)

    def StateChange(self):
        check1state = self.checkBox1.text() + '.isChecked=' + str(self.checkBox1.isChecked()) + ',CheckState=' + str(
            self.checkBox1.checkState()) + '\n'
        check2state = self.checkBox2.text() + '.isChecked=' + str(self.checkBox2.isChecked()) + ',CheckState=' + str(
            self.checkBox2.checkState()) + '\n'
        check3state = self.checkBox3.text() + '.isChecked=' + str(self.checkBox3.isChecked()) + ',CheckState=' + str(
            self.checkBox3.checkState()) + '\n'
        print(check1state+check2state+check3state)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.show()

    sys.exit(QApplication.exec_())
