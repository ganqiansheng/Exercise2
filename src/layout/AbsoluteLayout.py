import os
import sys
from PyQt5.QtCore import QUrl, QObject, pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel

class AbsoluteLayout(QWidget):
    def __init__(self):
        super(AbsoluteLayout, self).__init__()
        self.setWindowTitle('绝对布局')
        self.resize(600,300)

        self.label1=QLabel('欢迎',self)
        self.label1.move(15,20)

        self.label2=QLabel('欢迎',self)
        self.label2.move(25,50)

        self.label3=QLabel('欢迎',self)
        self.label3.move(35,80)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=AbsoluteLayout()
    main.show()

    sys.exit(app.exec_())




