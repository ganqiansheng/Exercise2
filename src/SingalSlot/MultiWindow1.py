from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys,time
from PyQt5 import QtCore
from functools import partial
from DateDialog import DateDialog

class MultiWindow1(QWidget):
    def __init__(self,parent=None):
        super(MultiWindow1, self).__init__(parent)
        self.setWindowTitle('多窗口间的信号传递-不使用信号和槽')

        self.lineEdit=QLineEdit(self)
        self.button1 = QPushButton('弹出对话框1')
        self.button1.clicked.connect(self.onButton1Click)

        self.button2 = QPushButton('弹出对话框2')
        self.button2.clicked.connect(self.onButton2Click)

        layout=QVBoxLayout()
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        self.setLayout(layout)


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
    main = MultiWindow1()
    main.show()

    sys.exit(app.exec_())

