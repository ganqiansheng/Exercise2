import os
import sys
from PyQt5.QtCore import QUrl, QObject, pyqtSlot, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtGui import *

class HBoxLayout(QWidget):
    def __init__(self):
        super(HBoxLayout, self).__init__()
        self.setWindowTitle('水平盒    布局')
        self.resize(600,300)

        layout=QHBoxLayout()

        palette=QPalette()

        label1=QLabel('欢迎')
        label1.setAutoFillBackground(True)
        palette.setColor(QPalette.Background,Qt.red)
        label1.setPalette(palette)
        # label1.setAlignment(self,Qt.AlignCenter)
        label2=QLabel('欢迎')
        label2.setAutoFillBackground(True)
        palette.setColor(QPalette.Background,Qt.gray)
        label2.setPalette(palette)
        label3=QLabel('欢迎')
        label3.setAutoFillBackground(True)
        palette.setColor(QPalette.Background,Qt.blue)
        label3.setPalette(palette)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.setSpacing(20)
        self.setLayout(layout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=HBoxLayout()
    main.show()

    sys.exit(app.exec_())




