import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

class QstackedWidgetDemo(QTabWidget):
    def __init__(self):
        super(QstackedWidgetDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('堆栈窗口控件演示案例')
        self.resize(200,80)


        self.list=QListWidget()
        self.list.insertItem(0,'联系方式')
        self.list.insertItem(1,'个人信息')
        self.list.insertItem(2,'教育程序')
        self.list.setFont(QFont('微软雅黑',12))

        self.stack1=QWidget()
        self.stack2=QWidget()
        self.stack3=QWidget()

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        self.stack=QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        hbox=QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addWidget(self.stack)

        self.setLayout(hbox)

        self.list.currentRowChanged.connect(self.display)


    def tab1UI(self):
        layout=QFormLayout()
        layout.addRow('姓名',QLineEdit())
        layout.addRow('地址',QLineEdit())

        self.stack1.setLayout(layout)

    def tab2UI(self):
        layout=QFormLayout()
        sex=QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow('性别',sex)
        layout.addRow('生日',QLineEdit())

        self.stack2.setLayout(layout)

    def tab3UI(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))

        self.stack3.setLayout(layout)

    def display(self,index):
        self.stack.setCurrentIndex(index)












if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QstackedWidgetDemo()
    main.show()

    sys.exit(app.exec_())

