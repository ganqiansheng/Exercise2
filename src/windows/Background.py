import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle('设置背景图片')
win.resize(350,250)
win.setObjectName('MainWindow')
# QSS
# win.setStyleSheet('#MainWindow{background:gray}')
# win.setStyleSheet('#MainWindow{border-image:url(./images/solutioncover.png)}')

#Qpalette
palette=QPalette()
# palette.setBrush(QPalette.Background,QBrush(QPixmap('./images/solutioncover.png')))
palette.setColor(QPalette.Background,Qt.lightGray)
win.setPalette(palette)


win.show()
sys.exit(app.exec_())

