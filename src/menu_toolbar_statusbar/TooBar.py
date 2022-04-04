

import sys

from PyQt5.QtCore import QMimeData
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ToolBar(QMainWindow):
    def __init__(self):
        super(ToolBar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('菜单演示案例')
        self.resize(600,400)

        # self.toolBar = QtWidgets.QToolBar(MainWindow)
        # self.toolBar.setObjectName("toolBar")
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        # addToolBar(self, Qt.ToolBarArea, QToolBar)
        # addToolBar(self, QToolBar)
        # addToolBar(self, str) -> QToolBar

        self.toolBar=QToolBar('file')
        # self.tb.setObjectName('file')
        self.addToolBar(Qt.TopToolBarArea,self.toolBar)



        self.actionNew = QAction('new',self)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.setIcon(QIcon('./fileico/filenew.ico'))
        self.toolBar.addAction(self.actionNew)

        self.actionOpen=QAction(QIcon('./fileico/fileopen.ico'),'Open',self)
        self.toolBar.addAction(self.actionOpen)

        self.actionSave=QAction(QIcon('./fileico/filesave.ico'),'Save',self)
        self.toolBar.addAction(self.actionSave)

        self.actionSaveas=QAction(QIcon('./fileico/filesaveas.ico'),'Save As',self)
        self.toolBar.addAction(self.actionSaveas)

        self.toolBar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

    #     self.btn=QPushButton('test',self)
    #     self.btn.move(150,150)
    #     self.btn.clicked.connect(self.btnClick)
    #
    # def btnClick(self):
    #     windonw=ToolBar()
    #     windonw.resize(300,200)
    #     windonw.show()
    #






if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ToolBar()
    main.show()

    sys.exit(QApplication.exec_())
