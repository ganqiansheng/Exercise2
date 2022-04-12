import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math


class Background2(QWidget):
    def __init__(self):
        super(Background2, self).__init__()
        self.setWindowTitle('绘制背景图片')

    def paintEvent(self, event):
        rect = self.getRect()

        painter = QPainter(self)  # 没有self,在屏幕上就不会显示
        # pixmap = QPixmap('./images/solutioncover.png')
        # painter.drawPixmap(rect, pixmap)
        painter.setBrush(Qt.lightGray)
        painter.drawRect(rect)

    def getRect(self):
        a=1.9
        x = math.floor(self.width() * (2-a)) / 2
        y = math.floor(self.height() * (2-a)) / 2
        width = self.width()-2 * x
        height = self.height()-2 * y
        return QRect(x, y, width, height)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Background2()
    main.show()

    sys.exit(app.exec_())
