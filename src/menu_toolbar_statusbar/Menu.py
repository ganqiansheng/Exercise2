

import sys

from PyQt5.QtCore import QMimeData
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Menu(QDialog):
    def __init__(self):
        super(Menu, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('菜单演示案例')

        bar=QMenuBar(self)

        file=bar.addMenu('文件')
        file.addAction('新建')


        open=QAction('打开',self)
        open.setShortcut('ctrl+O')
        file.addAction(open)

        save=QAction('保存',self)
        save.setShortcut('ctrl+S')
        file.addAction(save)
        save.triggered.connect(self.process)

        saveas=QAction('另存为',self)
        saveas.setShortcut('ctrl+A')
        file.addAction(saveas)

        edit=file.addMenu('edit')

        copy = QAction('复制',self)
        copy.setShortcut('ctrl+C')
        edit.addAction(copy)

        opreation=edit.addMenu('专业操作')

        cut = QAction('保存',self)
        cut.setShortcut('ctrl+U')
        edit.addAction(save)

        paste = QAction('粘贴',self)
        paste.setShortcut('ctrl+P')
        edit.addAction(paste)

        opreation1=QAction('专业操作',self)
        opreation.addAction(opreation1)
        opreation1.triggered.connect(self.process)




    def process(self,a):
        print(self.sender().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Menu()
    main.show()

    sys.exit(QApplication.exec_())
