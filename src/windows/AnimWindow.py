from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, time
from CommonHelper import CommonHelper

class AnimWindow(QMainWindow):
    def __init__(self):
        super(AnimWindow, self).__init__()
        self.setWindowTitle('动态改变窗口尺寸')
        self.OrigHeight=200
        self.ChangeHeight=1000
        self.setGeometry(QRect(500,100,1000,self.OrigHeight))
        self.btn=QPushButton('展开',self)
        self.btn.setGeometry(10,10,60,35)
        self.btn.clicked.connect(self.change)

        self.testButton=QPushButton('移动按钮',self)
        self.testButton.move(50,50)
        self.testButton.setGeometry(100,100,250,50)
        self.testButton.clicked.connect(self.startAnimation)
        self.lx=100
        self.ly=100
        self.oldWidth=100
        self.oldHeight=50


    def change(self):
        currentHeight = self.height()
        if self.OrigHeight == currentHeight:
            startHeight = self.OrigHeight
            endHeight = self.ChangeHeight
            self.btn.setText('收缩')
        else:
            startHeight = self.ChangeHeight
            endHeight = self.OrigHeight
            self.btn.setText('展开')

        self.animation=QPropertyAnimation(self,b'geometry')
        self.animation.setDuration(500)
        self.animation.setStartValue(QRect(500,100,1000,startHeight))
        self.animation.setEndValue(QRect(500,100,1000,endHeight))

        self.animation.start()

    def startAnimation(self):
        startpos = self.testButton.geometry()
        currentX=startpos.x()
        if currentX==self.lx:
            #按钮在左上方
            self.testButton.setText('移动按钮，向右下方移动')
            newpos = QRect(startpos.x() + 500, startpos.y() + 500, startpos.width()+100, startpos.height())
        elif currentX != self.lx:
            #按钮在左上方
            self.testButton.setText('移动按钮，向左上方移动')
            newpos = QRect(startpos.x() - 500, startpos.y() - 500, startpos.width()-100, startpos.height())

        animation = QPropertyAnimation(self.testButton, b"geometry", self)
        # animation.setTargetObject(self.testButton)
        # animation.setPropertyName(b"geometry")

        # animation.setStartValue(startpos)
        animation.setEndValue(newpos)
        animation.setDuration(1000)
        animation.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AnimWindow()
    qssStyle = '''
        QPushButton[name='btn2']{
            background-color:gray;
            color:yellow;
            height:120;
            font-size:48;
        }
        QPushButton[name='btn3']{
            background-color:blue;
            color:red;
            height:30;
            font-size:18;
        }
    '''
    main.setStyleSheet(qssStyle)
    main.show()

    sys.exit(app.exec_())
