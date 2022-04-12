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

        layout=QVBoxLayout()
        btn = QPushButton('关闭窗口',self)
        btn.clicked.connect(self.close)
        layout.addWidget(btn)
        self.setLayout(layout)

        self.pix =QBitmap('./images/mask.png')
        self.resize(self.pix.size())
        self.setMask(self.pix)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),QPixmap('./images/screen1.jpg'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AbnormitWindow()
    main.show()

    sys.exit(app.exec_())
