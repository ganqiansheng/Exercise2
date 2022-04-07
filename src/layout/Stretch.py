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
        self.setWindowTitle('设置伸缩量')
        self.resize(600,300)

        layout=QHBoxLayout()
        button1=QPushButton('按钮1')
        button2=QPushButton('按钮2')
        button3=QPushButton('按钮3')
        button4=QPushButton('按钮4')
        button5=QPushButton('按钮5')
        button6=QPushButton('按钮6')

        layout.addStretch(0)

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)

        layout.addStretch(1)
        layout.addWidget(button5)
        layout.addWidget(button6)

        layout2=QHBoxLayout()
        layout2.addStretch(1)
        button7=QPushButton('按钮7')
        button8=QPushButton('按钮8')
        button9=QPushButton('按钮9')

        layout2.addWidget(button7)
        layout2.addWidget(button8)
        layout2.addWidget(button9)

        mainLayout=QVBoxLayout()
        mainLayout.addLayout(layout)
        mainLayout.addLayout(layout2)
        # layout.addWidget(button1,1,Qt.AlignLeft|Qt.AlignTop)
        # layout.addWidget(button2,1,Qt.AlignLeft|Qt.AlignTop)
        # layout.addWidget(button3,1,Qt.AlignLeft|Qt.AlignTop)
        # layout.addWidget(button4,1,Qt.AlignHCenter|Qt.AlignVCenter)
        # layout.addWidget(button5,1,Qt.AlignHCenter|Qt.AlignBottom)

        # layout.setSpacing(20)
        self.setLayout(mainLayout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=HBoxLayout()
    main.show()

    sys.exit(app.exec_())




