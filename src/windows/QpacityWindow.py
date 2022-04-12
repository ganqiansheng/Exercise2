import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math


class QpacityWindow(QWidget):
    def __init__(self):
        super(QpacityWindow, self).__init__()
        self.setWindowTitle('创建透明半透明窗口')
        self.resize(300,200)
        self.setWindowOpacity(0.5)
        button=QPushButton('我的按钮',self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QpacityWindow()
    main.show()

    sys.exit(app.exec_())
