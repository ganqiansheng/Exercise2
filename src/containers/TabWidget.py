import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

class TabWidgetDemo(QTabWidget):
    def __init__(self):
        super(TabWidgetDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('选项卡演示案例')
        self.resize(600,400)

        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()

        self.addTab(self.tab1,'选项卡1')
        self.addTab(self.tab2,'选项卡2')
        self.addTab(self.tab3,'选项卡3')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()


    def tab1UI(self):
        layout=QFormLayout()
        layout.addRow('姓名',QLineEdit())
        layout.addRow('地址',QLineEdit())
        self.setTabText(0,'联系方式')

        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout=QFormLayout()
        sex=QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow('性别',sex)
        layout.addRow('生日',QLineEdit())
        self.setTabText(1,'个人详细信息')

        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))

        self.setTabText(2,'教育程序')
        self.tab3.setLayout(layout)








if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TabWidgetDemo()
    main.show()

    sys.exit(app.exec_())

