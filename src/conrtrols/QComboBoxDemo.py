#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class QComboBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 50)
        self.setWindowTitle('下拉列表控件演示')

        layout = QVBoxLayout()
        palette=QPalette()


        self.label=QLabel('请选择编程语言：')
        self.label.resize(self.label.width(),5)
        self.label.setAutoFillBackground(True)
        palette.setColor(QPalette.Window,Qt.lightGray)
        self.label.setPalette(palette)
        layout.addWidget(self.label)


        self.cb=QComboBox()
        self.cb.setAutoFillBackground(True)
        palette.setColor(QPalette.Window,Qt.magenta)
        self.cb.setPalette(palette)
        self.cb.addItem('C++')
        self.cb.addItem('VBasic')
        self.cb.addItems(['Delphi','C#','Python','Ruby','JAVA'])
        self.cb.currentIndexChanged.connect(self.SelectionChange)
        layout.addWidget(self.cb)

        self.setLayout(layout)

    def SelectionChange(self,i):
        cb=self.sender()
        self.label.setText('请选择编程语言：'+cb.currentText())
        for count in range(cb.count()):
            print('item'+str(count)+':'+cb.itemText(count))
        print('当前所选项是：'+cb.currentText() + '     当前的索引值为：'+str(i))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()

    sys.exit(QApplication.exec_())
