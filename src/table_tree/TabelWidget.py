import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TableWidgetDemo(QMainWindow):
    def __init__(self):
        super(TableWidgetDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TableView演示案例')
        self.resize(600,400)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['姓名','年龄','籍贯'])
        self.tableWidget.setVerticalHeaderLabels(['第1行','第2行','第3行','第4行'])

        nameItem=QTableWidgetItem('adam')
        self.tableWidget.setItem(0,0,nameItem)
        ageItem=QTableWidgetItem('24')
        self.tableWidget.setItem(0,1,ageItem)
        jgItem=QTableWidgetItem('浙江')
        self.tableWidget.setItem(0,2,jgItem)
        nameItem=QTableWidgetItem('jonathan')
        self.tableWidget.setItem(1,0,nameItem)
        ageItem=QTableWidgetItem('29')
        self.tableWidget.setItem(1,1,ageItem)
        jgItem=QTableWidgetItem('上海')
        self.tableWidget.setItem(1,2,jgItem)
        nameItem=QTableWidgetItem('jickie')
        self.tableWidget.setItem(2,0,nameItem)
        ageItem=QTableWidgetItem('34')
        self.tableWidget.setItem(2,1,ageItem)
        jgItem=QTableWidgetItem('浙江')
        self.tableWidget.setItem(2,2,jgItem)

        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tableWidget.resizeRowToContents(0)
        self.tableWidget.resizeColumnToContents(0)
        self.tableWidget.resizeColumnToContents(1)
        self.tableWidget.resizeColumnToContents(2)

        # Custom = 2
        # Fixed = 2
        # Interactive = 0
        # ResizeToContents = 3
        # Stretch = 1

        self.tableWidget.horizontalHeader().setVisible(True)

        self.tableWidget.setShowGrid(False)





    def tabelViewclicked(self,index):
        print(type(index))

        # print(self.tableView.index




if __name__=='__main__':
    app=QApplication(sys.argv)
    main=TableWidgetDemo()
    main.show()

    sys.exit(app.exec_())