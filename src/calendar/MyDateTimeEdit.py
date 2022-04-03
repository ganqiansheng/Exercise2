

import sys

from PyQt5.QtCore import QMimeData, QDate, Qt, QDateTime, QTime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyDateTimeEdit(QDialog):
    def __init__(self):
        super(MyDateTimeEdit, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('日历演示案例')
        self.resize(400,180)

        layout=QVBoxLayout()
        myDateTime1 = QDateTimeEdit(QDateTime.currentDateTime())
        myDateTime1.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        myDateTime1.setMinimumDate(QDate.currentDate().addDays(-365))
        myDateTime1.setMaximumDate(QDate.currentDate().addDays(+365))
        myDateTime1.dateChanged.connect(self.onDateChanged)
        myDateTime1.timeChanged.connect(self.onTimeChanged)
        myDateTime1.dateTimeChanged.connect(self.onDateTimeChanged)

        myDateTime2 = QDateTimeEdit(QDateTime.currentDateTime())
        myDateTime2.setCalendarPopup(True)
        myDateTime2.setDisplayFormat('yyyy/MM/dd HH-mm-ss')
        myDateTime2.dateChanged.connect(self.onDateChanged)
        myDateTime2.timeChanged.connect(self.onTimeChanged)
        myDateTime2.dateTimeChanged.connect(self.onDateTimeChanged)

        myDateTime3 = QDateTimeEdit(QDate.currentDate())
        myDateTime3.setDisplayFormat('yyyy.MM.dd')

        myDateTime4 = QDateTimeEdit(QTime.currentTime())
        myDateTime4.setDisplayFormat('HH:mm:ss')

        layout.addWidget(myDateTime1)
        layout.addWidget(myDateTime2)
        layout.addWidget(myDateTime3)
        layout.addWidget(myDateTime4)

        self.setLayout(layout)

    def onDateChanged(self,date):
        print('data changed:'+date.toString('yyyy-MM-dd HH:mm:ss dddd'))

    def onTimeChanged(self, time):
        print('Time Changed:'+time.toString('HH:mm:ss'))


    def onDateTimeChanged(self, datetime):
        print('DateTime Changed:'+datetime.toString('yyyy-MM-dd HH:mm:ss dddd'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyDateTimeEdit()
    main.show()

    sys.exit(QApplication.exec_())
