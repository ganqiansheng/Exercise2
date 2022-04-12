import sys,time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math


class AbnormitWindow(QWidget):
    def __init__(self):
        super(AbnormitWindow, self).__init__()
        self.setWindowTitle('绘制异形窗口')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.i=1
        self.mypix()
        self.timer=QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.timeChange)
        self.timer.start()



        # self.pix =QBitmap('./images/mask.png')
        # self.resize(self.pix.size())
        # self.setMask(self.pix)

    def timeChange(self):
        self.i += 1
        self.mypix()

    def mypix(self):
        self.update()
        if self.i ==5:
            self.i = 1
        self.myPic={1:'./images/up.png',2:'./images/right.png',3:'./images/down.png',4:'./images/left.png'}
        self.pix=QPixmap(self.myPic[self.i])
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.dragPosition = None


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
