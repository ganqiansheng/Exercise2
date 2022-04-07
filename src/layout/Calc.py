import os
import sys
from PyQt5.QtCore import QUrl, QObject, pyqtSlot, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtGui import *

class CalcDemo(QWidget):
    def __init__(self):
        super(CalcDemo, self).__init__()
        self.setWindowTitle('计算器')
        self.resize(600,300)

        layout=QGridLayout()
        self.setLayout(layout)

        names = ['CLS','Back','','Close',
                 '7','8','9','+',
                 '4','5','6','-',
                 '1','2','3','*',
                 '0','.','=','/']

        positions = [(i,j) for i in range(5) for j in range(4)]
        for position,name in zip(positions,names):
            print(position,name)
            if name=='':
                continue
            button=QPushButton(name)
            layout.addWidget(button,*position)







if __name__=='__main__':
    app=QApplication(sys.argv)
    main=CalcDemo()
    main.show()

    sys.exit(app.exec_())




