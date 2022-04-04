import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ListWidget(QMainWindow):
    def __init__(self):
        super(ListWidget, self).__init__()
        self.initUI()


    def initUI(self):
        self.resize(1000,800)

        self.listWidget=QListWidget(self)
        self.listWidget.resize(400,300)
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')
        self.listWidget.addItem('item4')
        self.listWidget.addItem('item5')
        self.listWidget.itemClicked.connect(self.clicked)

        self.setCentralWidget(self.listWidget)

    def clicked(self,index):
        QMessageBox.information(self,'ListWidget提示','你选中了'+self.listWidget.item(self.listWidget.row(index)).text())










if __name__=='__main__':
    app=QApplication(sys.argv)
    main=ListWidget()
    main.show()

    sys.exit(app.exec_())