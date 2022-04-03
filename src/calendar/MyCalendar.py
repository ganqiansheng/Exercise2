

import sys

from PyQt5.QtCore import QMimeData, QDate,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyCalendar(QDialog):
    def __init__(self):
        super(MyCalendar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('日历演示案例')
        self.resize(400,180)
        self.calendar=QCalendarWidget(self)
        self.calendar.setMinimumDate(QDate(1990,1,1))
        self.calendar.setMaximumDate(QDate(2050,12,31))

        layout1 = QFormLayout()
        layout2 = QVBoxLayout()
        self.calendar.setGridVisible(True)
        # self.calendar.move(200,200)

        # palette=QPalette()
        # palette.setColor(QPalette.Window, Qt.gray)
        # palette.setColor(QPalette.window,Qt.lightGray)


        # self.frame.setAutoFillBackground(True)
        # self.frame.setPalette(palette)

        self.btnGrid=QPushButton('隐藏网格线')
        self.btnGrid.clicked.connect(self.ShowGrid)
        layout2.addWidget(self.btnGrid)

        self.btn2=QPushButton('其他功能键')
        layout2.addWidget(self.btn2)
        self.btnExit=QPushButton('退出')
        self.btnExit.clicked.connect(self.QuitApp)
        layout2.addWidget(self.btnExit)
        self.label=QLabel('当前选中的日期')
        layout2.addWidget(self.label)

        self.calendar.clicked.connect(self.ShowDate)


        layout1.addRow(self.calendar,layout2)


        self.setLayout(layout1)

    def ShowGrid(self):
        # print(type(self))
        if self.btnGrid.text()=='显示网格线':
            self.btnGrid.setText('隐藏网格线')
            self.calendar.setGridVisible(True)
        else:
            self.btnGrid.setText('显示网格线')
            self.calendar.setGridVisible(False)

    def QuitApp(self):
        app=QApplication.instance()
        app.quit()

    def ShowDate(self,date):
        # self.label.setText(date.toString('yyyy-MM-dd dddd'))
        self.label.setText(self.calendar.selectedDate().toString('yyyy-MM-dd dddd'))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyCalendar()
    main.show()

    sys.exit(QApplication.exec_())
