import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter,QColor,QFont



class DrawTextDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(300, 400)
        self.text='Python从菜鸟到高手'

    def paintEvent(self, QPaintEvent):
        painter=QPainter(self)
        painter.begin(self)
        painter.setPen(QColor(255,0,255))
        painter.setFont(QFont('Microsoft JhengHei Light',22))
        painter.drawText(QPaintEvent.rect(),Qt.AlignCenter,self.text)


        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawTextDemo()
    main.show()

    sys.exit(QApplication.exec_())
