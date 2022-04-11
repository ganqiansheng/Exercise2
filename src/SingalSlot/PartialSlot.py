# from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys,time
from PyQt5 import QtCore
from functools import partial

class PartialSlotArg(QMainWindow):
    def __init__(self):
        super(PartialSlotArg, self).__init__()

        self.setWindowTitle('用partial表达式为槽函数传递参数')
        button1=QPushButton("按钮1")
        button2=QPushButton('按钮2')

        layout =QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        mainlayout=QWidget()
        mainlayout.setLayout(layout)
        self.setCentralWidget(mainlayout)
        m=10
        n=39
        # button1.clicked.connect(lambda:self.on_buttonClicked(m,n))
        # button2.clicked.connect(lambda :self.on_buttonClicked(m,-1*n))

        button1.clicked.connect(partial(self.on_buttonClicked,m,n))
        button2.clicked.connect(partial(self.on_buttonClicked,m,-1*n))


    def on_buttonClicked(self,m,n):
        print('m+n=',str(m+n))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PartialSlotArg()
    main.show()

    sys.exit(app.exec_())

