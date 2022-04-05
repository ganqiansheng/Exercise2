import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

class DockWidgetDemo(QMainWindow):
    def __init__(self):
        super(DockWidgetDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('堆栈窗口控件演示案例')
        self.resize(800,600)

        # layout=QHBoxLayout()
        self.items=QDockWidget()
        self.list=QListWidget()
        self.list.addItem('item1')
        self.list.addItem('item2')
        self.list.addItem('item3')

        self.items.setWidget(self.list)

        self.setCentralWidget(QLineEdit())
        self.items.setFloating(True)

        self.addDockWidget(Qt.RightDockWidgetArea,self.items)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DockWidgetDemo()
    main.show()

    sys.exit(app.exec_())

