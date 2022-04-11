from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys,time
from PyQt5 import QtCore
from functools import partial


class NewDateDialog(QDialog):
    signalCustom = pyqtSignal(str)
    def __init__(self,parent=None):
        super(NewDateDialog, self).__init__(parent)
        self.setWindowTitle('子窗口：用于发射信号')
        layout=QVBoxLayout()
        self.label=QLabel('前者发射内置信号\n后者发射自定义信号')
        self.datetime_inner = QDateEdit(self)
        self.datetime_inner.setCalendarPopup(True)
        self.datetime_inner.setDisplayFormat('yyyy-mm-dd hh:mm:ss')

        self.datetime_custom= QDateEdit(self)
        self.datetime_custom.setCalendarPopup(True)

        self.datetime_inner.setDateTime(QDateTime.currentDateTime())
        self.datetime_custom.setDateTime(QDateTime.currentDateTime())


        layout.addWidget(self.label)
        layout.addWidget(self.datetime_inner)
        layout.addWidget(self.datetime_custom)

        buttons=QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel,Qt.Horizontal,self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)
        self.setLayout(layout)

        self.datetime_custom.dateChanged.connect(self.emit_signalCustom)

    def emit_signalCustom(self):
        datestr=self.datetime_custom.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        self.signalCustom.emit(datestr)

    def dateTime(self):
        return self.datetime.dateTime()

    @staticmethod
    def getDateTime(parent=None):
        dialog=NewDateDialog(parent)
        result=dialog.exec()
        date=dialog.dateTime()
        return (date.date(),date.time(),result==QDialog.Accepted)


