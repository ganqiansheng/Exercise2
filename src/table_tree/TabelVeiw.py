import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TableView(QWidget):
    def __init__(self):
        super(TableView, self).__init__()
        self.initUI()

    def initUI(self):

        self.model=QStandardItemModel(4,3)
        self.model.setHorizontalHeaderLabels(['序号','姓名','年龄'])

        self.tableView=QTableView()

        self.tableView.setModel(self.model)

        layout=QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)

        item00=QStandardItem('1')
        item01=QStandardItem('jonathan')
        item02=QStandardItem('23')
        item20=QStandardItem('3')
        item21=QStandardItem('jessica')
        item22=QStandardItem('26')
        item10=QStandardItem('2')
        item11=QStandardItem('sam')
        item12=QStandardItem('28')
        self.model.setItem(0,0,item00)
        self.model.setItem(0,1,item01)
        self.model.setItem(0,2,item02)
        self.model.setItem(2,0,item20)
        self.model.setItem(2,1,item21)
        self.model.setItem(2,2,item22)
        self.model.setItem(1,0,item10)
        self.model.setItem(1,1,item11)
        self.model.setItem(1,2,item12)



if __name__=='__main__':
    app=QApplication(sys.argv)
    main=TableView()
    main.show()

    sys.exit(app.exec_())