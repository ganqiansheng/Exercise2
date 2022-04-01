#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout
class WidgetGeometry(QWidget):
    def __init__(self,parent=None):
        super(WidgetGeometry,self).__init__(parent)
        self.resize(300,200)

        self.widgetbutton=QPushButton('显示widget.x/y/width/height')
        self.widgetbutton.clicked.connect(self.onClickwidgetButton)
        self.widgetgeometrybutton=QPushButton('显示widget.geometry.x/y/width/height')
        self.widgetgeometrybutton.clicked.connect(self.onClickwidgetgeometrybutton)
        self.widgetframegeometrybutton=QPushButton('显示widget.framegeometry.x/y/width/height')
        self.widgetframegeometrybutton.clicked.connect(self.onClickwidgetframegeometrybutton)

        self.quitbutton=QPushButton('退出应用程序')
        self.quitbutton.clicked.connect(self.quitbutton)


        layout=QVBoxLayout()
        layout.addWidget(self.widgetbutton)
        layout.addWidget(self.widgetgeometrybutton)
        layout.addWidget(self.widgetframegeometrybutton)

        # mainFrame=s
        # mainFrame.setLayout(layout)
        self.setLayout(layout)


    # 显示widget.x/y/width/height
    def onClickwidgetButton(self):
        print('widget.x=%d'%self.x())
        print('widget.y=%d'%self.y())
        print('widget.width=%d'%self.width())
        print('widget.height=%d'%self.height())

    # 显示widget.geometry.x/y/width/height
    def onClickwidgetgeometrybutton(self):
        print('widget.geometry().x=%d'%self.geometry().x())
        print('widget.geometry().y=%d'%self.geometry().y())
        print('widget.geometry().width=%d'%self.geometry().width())
        print('widget.geometry().height=%d'%self.geometry().height())

    # 显示widget.framegeometry.x/y/width/height
    def onClickwidgetframegeometrybutton(self):
        print('widget.frameGeometry().x=%d'%self.frameGeometry().x())
        print('widget.frameGeometry().y=%d'%self.frameGeometry().y())
        print('widget.frameGeometry().width=%d'%self.frameGeometry().width())
        print('widget.frameGeometry().height=%d'%self.frameGeometry().height())

    # 退出应用程序
    def quitbutton(self):
        app=QApplication.instance()
        app.quit()


if __name__=='__main__':
    app=QApplication(sys.argv)
    wedgit=WidgetGeometry()
    wedgit.show()

    sys.exit(QApplication.exec_())