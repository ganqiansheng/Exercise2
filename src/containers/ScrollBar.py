import sys,time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *


class ScrollsBarDemo(QWidget):
    def __init__(self):
        super(ScrollsBarDemo,self).__init__()

        self.resize(300,400)
        self.label=QLabel('显示当前时间')

        mainLayout=QHBoxLayout()
        self.label=QLabel('通过拖动滚动条来改变文字颜色')
        mainLayout.addWidget(self.label)

        layout=QHBoxLayout()
        self.scrollBar1 = QScrollBar()
        self.scrollBar2 = QScrollBar()
        self.scrollBar3 = QScrollBar()
        self.scrollBar4 = QScrollBar()

        self.scrollBar1.setMaximum(255)
        self.scrollBar2.setMaximum(255)
        self.scrollBar3.setMaximum(255)

        self.scrollBar1.valueChanged.connect(self.changeColor)
        self.scrollBar2.valueChanged.connect(self.changeColor)
        self.scrollBar3.valueChanged.connect(self.changeColor)
        self.scrollBar4.valueChanged.connect(self.moveLabel)

        layout.addWidget(self.scrollBar1)
        layout.addWidget(self.scrollBar2)
        layout.addWidget(self.scrollBar3)
        layout.addWidget(self.scrollBar4)

        mainLayout.addLayout(layout)

        self.setLayout(mainLayout)

    def changeColor(self,value):
        print(value)
        print(self.scrollBar1.value(),self.scrollBar2.value(),self.scrollBar3.value())
        c=QColor(self.scrollBar1.value(),self.scrollBar2.value(),self.scrollBar3.value())
        palette=QPalette()
        palette.setColor(QPalette.Foreground,c)
        self.label.setPalette(palette)

    def moveLabel(self,value):
        print(value)
        print(self.label.x(),self.y(),value)
        x=self.label.x()
        y=self.label.y()
        self.label.move(x,y+self.scrollBar4.value())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ScrollsBarDemo()
    main.show()

    sys.exit(app.exec_())
