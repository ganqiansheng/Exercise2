import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Background1(QWidget):
    def __init__(self):
        super(Background1, self).__init__()
        self.setWindowTitle('绘制背景颜色')
    def paintEvent(self, event):
        painter = QPainter(self)    #没有self,在屏幕上就不会显示
        painter.setBrush(Qt.darkYellow)
        painter.drawRect(self.rect())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Background1()
    main.show()

    sys.exit(app.exec_())
