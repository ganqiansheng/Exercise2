from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, time
from CommonHelper import CommonHelper

class QSSSelector(QMainWindow):
    def __init__(self):
        super(QSSSelector, self).__init__()
        self.setWindowTitle('加载QSS')
        self.resize(477, 258)
        btn=QPushButton('装载QSS文件')
        btn.setToolTip('这是一个提示')

        vbox=QVBoxLayout()
        vbox.addWidget(btn)

        mainFrame=QWidget(self)
        self.setCentralWidget(mainFrame)
        mainFrame.setLayout(vbox)

        btn.clicked.connect(self.onClick)

    def onClick(self):
        styleFile='./style.qss'
        qssStyle= CommonHelper.readQSS(styleFile)
        self.setStyleSheet(qssStyle)
        print(qssStyle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSSSelector()
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
