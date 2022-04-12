import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math

from pygments.formatters import img


class ScaleImage(QWidget):
    def __init__(self):
        super(ScaleImage, self).__init__()
        self.setWindowTitle('绘制异形窗口')
        self.resize(600,600)

        fileName='./images/Cloudy_72px.png'
        image=QImage(fileName)
        label1=QLabel(self)
        label1.setFixedWidth(400)
        label1.setFixedHeight(400)

        result = image.scaled(label1.width(),label1.height(),Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        label1.setPixmap(QPixmap.fromImage(result))


        layout=QVBoxLayout()
        layout.addWidget(label1)
        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ScaleImage()
    qssStyle='''
        QLabel{
            border-image:url('images/python.jpg');
            width:77;
            height:22;
        }
    '''
    main.setStyleSheet(qssStyle)

    main.show()

    sys.exit(app.exec_())
