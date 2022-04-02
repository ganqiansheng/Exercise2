import math
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont,QPen
import math


class DrawPiontDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(600, 400)
        self.text='Python从菜鸟到高手'

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QColor(255, 0, 255))
        painter.setFont(QFont('Microsoft JhengHei Light',22))
        size = self.size()

        for i in range(-1000,2000):
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width()) / 2.0 * math.pi / 50) + size.height() / 2.0
            painter.drawPoint(math.floor(x), math.floor(y))

        painter.drawText(event.rect(),Qt.AlignBottom,self.text)

        pen=QPen(Qt.magenta,2,Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(50,50,300,400)

        pen.setStyle(Qt.DotLine)
        pen.setColor(Qt.cyan)
        painter.setPen(pen)
        painter.drawLine(30,300,350,50)

        pen=QPen(Qt.magenta,2,Qt.CustomDashLine)
        pen.setDashPattern([2,6,10,3])
        painter.setPen(pen)
        painter.drawLine(50,50,300,50)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawPiontDemo()
    main.show()

    sys.exit(QApplication.exec_())
