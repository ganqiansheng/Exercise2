from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys,time
from PyQt5 import QtCore
from functools import partial
from NewDateDialog import NewDateDialog

class MultiWindow2(QWidget):
    def __init__(self,parent=None):
        super(MultiWindow2, self).__init__(parent)
        self.setWindowTitle('多窗口间的信号交互(2)-使用信号和槽')
        self.resize(400,100)

        layout=QVBoxLayout()

        self.lineEdit_inner=QLineEdit()
        self.lineEdit_inner.setPlaceholderText('接收子窗口内置信号的时间')
        self.lineEdit_emit=QLineEdit()
        self.lineEdit_emit.setPlaceholderText('接收子窗口自定义信号的时间')
        self.open_btn=QPushButton('获取时间')
        self.open_btn.clicked.connect(self.openDialog)

        layout.addWidget(self.lineEdit_inner)
        layout.addWidget(self.lineEdit_emit)
        layout.addWidget(self.open_btn)
        self.setLayout(layout)

    def openDialog(self):
        dialog=NewDateDialog(self)

        dialog.datetime_inner.dateChanged.connect(self.deal_inner_slot)
        dialog.signalCustom.connect(self.deal_emit_slot)

        dialog.show()

    def deal_inner_slot(self,date):
        self.lineEdit_inner.setText(date.toString())

    def deal_emit_slot(self,datestr):
        self.lineEdit_emit.setText(datestr)





    def onButton1Click(self):
        dialog=DateDialog(self)
        result=dialog.exec()
        date=dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        dialog.destroy()

    def onButton2Click(self):
        date,time,result =DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        if result==QDialog.Accepted:
            print('点击了确定按钮')
        else:
            print('点击了取消按钮')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MultiWindow2()
    main.show()

    sys.exit(app.exec_())

