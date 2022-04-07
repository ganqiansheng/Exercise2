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
        self.setWindowTitle('垂直盒    布局')
        self.resize(600,300)

        layout=QVBoxLayout()
        button1=QPushButton('按钮1')
        button2=QPushButton('按钮2')
        button3=QPushButton('按钮3')
        button4=QPushButton('按钮4')
        button5=QPushButton('按钮5')

        layout.addWidget(button1,1,Qt.AlignLeft|Qt.AlignTop)
        layout.addWidget(button2,1,Qt.AlignLeft|Qt.AlignTop)
        layout.addWidget(button3,1,Qt.AlignLeft|Qt.AlignTop)
        layout.addWidget(button4,1,Qt.AlignLeft|Qt.AlignTop)
        layout.addWidget(button5)

        # layout.addWidget(button1,1,Qt.AlignLeft|Qt.AlignTop)
        # layout.addWidget(button2,1,Qt.AlignLeft|Qt.AlignTop)
        # layout.addWidget(button3,1,Qt.AlignLeft|Qt.AlignTop)
        # layout.addWidget(button4,1,Qt.AlignHCenter|Qt.AlignVCenter)
        # layout.addWidget(button5,1,Qt.AlignHCenter|Qt.AlignBottom)

        # layout.setSpacing(20)
        self.setLayout(layout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=HBoxLayout()
    main.show()

    sys.exit(app.exec_())




