#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
from PyQt5.QtGui import QIcon

class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm,self).__init__()
        self.setWindowTitle('让窗口居中')
        self.resize(400,300)
        self.status=self.statusBar()
        self.status.showMessage('只存在5秒种',5000)
    def Center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        newLeft=(screen.width()-size.width())/2
        newTop=(screen.height()-size.height())/2
        self.move(newleft,newTop)

if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/0.ICO'))
    main=CenterForm()

    main.show()

    sys.exit(app.exec_())