import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *


class ScrollBar(QMainWindow):
    count = 0

    def __init__(self):
        super(ScrollBar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('堆栈窗口控件演示案例')
        self.resize(800, 600)

        mainLayout=QVBoxLayout()

        self.label=QLabel('拖动滚动条来改变文字颜色')
        mainLayout.addWidget(self.label)

        layout=QHBoxLayout()

        self.scrollBar1 = QScrollBar()
        self.scrollBar1.setMaximum(255)
        self.scrollBar1.sliderMoved.connect(self.sliderMoved)

        self.scrollBar2 = QScrollBar()
        self.scrollBar2.setMaximum(255)
        self.scrollBar2.sliderMoved.connect(self.sliderMoved)

        self.scrollBar3 = QScrollBar()
        self.scrollBar3.setMaximum(255)
        self.scrollBar3.sliderMoved.connect(self.sliderMoved)

        self.scrollBar4 = QScrollBar()
        self.scrollBar4.setMaximum(255)
        self.scrollBar4.sliderMoved.connect(self.sliderMoved1)

        layout.addWidget(self.scrollBar1)
        layout.addWidget(self.scrollBar2)
        layout.addWidget(self.scrollBar3)
        layout.addWidget(self.scrollBar4)


        mainLayout.addLayout(layout)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(mainLayout)

    def sliderMoved(self):
        print(self.scrollBar1.value(),self.scrollBar2.value(),self.scrollBar3.value())
        palette=QPalette()
        c=QColor(self.scrollBar1.value(),self.scrollBar2.value(),self.scrollBar3.value(),255)
        palette.setColor(QPalette.Foreground,c)
        self.label.setPalette(palette)
    def sliderMoved1(self):
        self.label.move(self.label.x(),self.y()+self.scrollBar4.value())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ScrollBar()
    main.show()

    sys.exit(app.exec_())
