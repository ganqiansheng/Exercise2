import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math


class AbnormitWindow(QWidget):
    def __init__(self):
        super(AbnormitWindow, self).__init__()
        self.setWindowTitle('绘制异形窗口')
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint)
        # self.setWindowState(Qt.WindowFullScreen)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.lastPoint = QPoint()
        self.endPoint = QPoint()

        # layout=QVBoxLayout()
        # btn = QPushButton('关闭窗口',self)
        # btn.clicked.connect(self.close)
        # layout.addWidget(btn)
        # self.setLayout(layout)

        self.pix =QBitmap('./images/mask.png')
        self.resize(self.pix.size())
        self.setMask(self.pix)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),QPixmap('./images/screen1.jpg'))

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_Drag=True
        self.m_DragPosition = event.globalPos()-self.pos()
        self.setCursor(QCursor(Qt.OpenHandCursor))
        if event.button()==Qt.RightButton:
            self.close()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and  self.m_Drag:
            self.move(event.globalPos()-self.m_DragPosition)

    def mouseReleaseEvent(self, event):
        self.m_Drag=False
        self.setCursor(QCursor(Qt.ArrowCursor))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AbnormitWindow()
    main.show()

    sys.exit(app.exec_())
