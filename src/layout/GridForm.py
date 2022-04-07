import os
import sys
from PyQt5.QtCore import QUrl, QObject, pyqtSlot, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtGui import *

class GridFormDemo(QWidget):
    def __init__(self):
        super(GridFormDemo, self).__init__()
        self.setWindowTitle('栅格布局：表单设计')
        self.resize(350,300)

        titleLabel=QLabel('标题')
        authorLabel=QLabel('作者')
        contentLabel=QLabel('内容')

        titleLineEdit=QLineEdit()
        authorLineEdit=QLineEdit()
        contentTextEdit=QTextEdit()

        grid=QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)

        grid.addWidget(titleLabel,0,0)
        grid.addWidget(titleLineEdit,0,1)
        grid.addWidget(authorLabel,1 ,0)
        grid.addWidget(authorLineEdit,1,1)
        grid.addWidget(contentLabel,2,0)
        grid.addWidget(contentTextEdit,2,1,5,1)




if __name__=='__main__':
    app=QApplication(sys.argv)
    main=GridFormDemo()
    main.show()

    sys.exit(app.exec_())




