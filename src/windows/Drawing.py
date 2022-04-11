from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, time


class Drawing(QWidget):
    signalResize = pyqtSignal(int,int)
    def __init__(self):
        super(Drawing, self).__init__()
        self.setWindowTitle('绘图应用')
        self.resize(600, 600)

        self.oldWidth = self.geometry().width()
        self.oldHeight = self.geometry().height()

        self.pix=QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()

        self.backColor = Qt.white

        self.initUI()

        self.signalResize.connect(self.pipmapResize)
        # self.resizeEvent.connect(self.myWindowResize)

    def resizeEvent(self, event):

        width=self.geometry().width()
        height=self.geometry().height()
        self.signalResize.emit(width,height)

    def pipmapResize(self,width,height):
        self.pix=QPixmap(width,height)
        self.pix.fill(self.backColor)


        self.oldWidth = width
        self.oldHeight = height


    def initUI(self):
        self.pix=QPixmap(600,600)
        self.pix.fill(self.backColor)

    def paintEvent(self, event):
        pp = QPainter(self.pix)
        if self.lastPoint != self.endPoint:
            pp.drawLine(self.lastPoint,self.endPoint)

        self.lastPoint = self.endPoint
        painter = QPainter(self)
        painter.drawPixmap(0,0,self.pix)

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()  #调用一次 paintEvent

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()





        #
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint
        #                     | Qt.WindowCloseButtonHint |
        #                     Qt.WindowMinimizeButtonHint)
        #
        # layout = QVBoxLayout()
        # maxButton1 = QPushButton('窗口最大化1')
        # maxButton1.clicked.connect(self.maximized1)
        #
        #
        # maxButton2 = QPushButton('窗口最大化2')
        # maxButton2.clicked.connect(self.showMaximized)
        #
        # minButton = QPushButton('窗口最小化')
        # minButton.clicked.connect(self.showMinimized)
        #
        # layout.addWidget(maxButton1)
        # layout.addWidget(maxButton2)
        # layout.addWidget(minButton)
        # self.setLayout(layout)

    def maximized1(self):
        desktop = QApplication.desktop()
        rect = desktop.availableGeometry()

        self.setGeometry(rect)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Drawing()
    main.show()

    sys.exit(app.exec_())
