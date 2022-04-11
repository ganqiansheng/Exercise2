from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys,time
from PyQt5 import QtCore
from functools import partial
class OverrideSlot(QMainWindow):
    def __init__(self):
        super(OverrideSlot, self).__init__()

        self.setWindowTitle('用Override覆盖槽函数')
    def keyPressEvent(self, e):
        if e.key()==Qt.Key_Escape:
            self.close()
        elif e.key()== Qt.Key_Alt:
            self.setWindowTitle('按钮ALT被按下')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = OverrideSlot()
    main.show()

    sys.exit(app.exec_())

