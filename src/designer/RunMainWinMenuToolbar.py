#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
import MainWinMenuToolbar
from  PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui=MainWinMenuToolbar.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
