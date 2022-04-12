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

        # '
        # QMainWindow
        # {
        #     border - image: url(\'./images/python.jpg\')
        # }
        # QToolTip
        # {
        #     border: 2px solid rgb(45, 45, 45);
        # background: white;
        # font - size: 30
        # px;
        # color: red
        # }
        # '

        # 'QMainWindow{
        # border - image: url(\'./images/python.jpg\')
        # }
        # QToolTip
        # {
        #     border: 2px solid rgb(45, 45, 45);
        # background: white
        # font: 30
        # pt
        # color: red
        # }'

        # btn1 = QPushButton('按钮1', self)
        # btn2 = QPushButton('按钮2', self)
        # btn2.setProperty('name','btn2')
        # btn3 = QPushButton('按钮3', self)
        # btn3.setProperty('name','btn3')
        # btn4 = QPushButton('按钮4', self)
        #
        # layout = QVBoxLayout()
        # layout.addWidget(btn1)
        # layout.addWidget(btn2)
        # layout.addWidget(btn3)
        # layout.addWidget(btn4)
        # self.setLayout(layout)


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
