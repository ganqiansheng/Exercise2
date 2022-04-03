import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class FillRect(QWidget):
    def __init__(self):
        super(FillRect, self).__init__()
        self.intiUI()

    def intiUI(self):
        self.setWindowTitle('画刷功能演示')
        self.resize(660,800)
        self.move(1770,100)

    def paintEvent(self,e):
        qp=QPainter()
        qp.begin(self)
        brush=QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(10,10,90,50)
        #=============================
        brush=QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(110,10,90,50)

        brush=QBrush(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(210,10,90,50)

        brush=QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(310,10,90,50)

        brush=QBrush(Qt.Dense3Pattern)
        qp.setBrush(brush)
        qp.drawRect(410,10,90,50)

        brush=QBrush(Qt.Dense4Pattern)
        qp.setBrush(brush)
        qp.drawRect(510,10,90,50)

        brush=QBrush(Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(10,70,90,50)

        brush=QBrush(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(110,70,90,50)

        brush=QBrush(Qt.Dense7Pattern)
        qp.setBrush(brush)
        qp.drawRect(210,70,90,50)
        #=============================
        brush=QBrush(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(310,70,90,50)

        brush=QBrush(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(410,70,90,50)

        brush=QBrush(Qt.CrossPattern)
        qp.setBrush(brush)
        qp.drawRect(510,70,90,50)

        brush=QBrush(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(10,130,90,50)

        brush=QBrush(Qt.FDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(110,130,90,50)

        brush=QBrush(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(210,130,90,50)

        brush=QBrush(Qt.LinearGradientPattern)
        qp.setBrush(brush)
        qp.drawRect(310,130,90,50)

        brush=QBrush(Qt.RadialGradientPattern)
        qp.setBrush(brush)
        qp.drawRect(410,130,90,50)

        brush=QBrush(Qt.ConicalGradientPattern)
        qp.setBrush(brush)
        qp.drawRect(510,130,90,50)

        brush=QBrush(Qt.TexturePattern)
        qp.setBrush(brush)
        qp.drawRect(10,190,90,50)




        qp.end()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FillRect()
    main.show()

    sys.exit(QApplication.exec_())
