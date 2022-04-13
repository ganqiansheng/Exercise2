from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class DataGridShow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(400,500)
        layout=QVBoxLayout()
        self.tableView=QTableView()
        self.buttonAdd=QPushButton('添加一行')
        self.buttonAdd.clicked.connect(AddRow)
        self.buttonDel=QPushButton('删除一行')
        self.buttonDel.clicked.connect(DelRow)
        layout.addWidget(self.tableView)
        layout.addWidget(self.buttonAdd)
        layout.addWidget(self.buttonDel)
        self.setLayout(layout)

def initDatabase():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./db/database.db')

def initModel(model):
    model.setTable('people')
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0,Qt.Horizontal,'序号')
    model.setHeaderData(1,Qt.Horizontal,'姓名')
    model.setHeaderData(2,Qt.Horizontal,'地址')

def initView(tableView):
    tableView.setModel(model)

def AddRow():
    ret = model.insertRows(model.rowCount(),1)
    # print('model.insertRows(model.rowCount(),1)的返回值是：' + str(ret)）


def DelRow():
    if not dataGrid.tableView.currentIndex() :
        QMessageBox.about(dataGrid,'提示','没有选中行')
        return False
    ret = model.removeRow(dataGrid.tableView.currentIndex().row())
    tableViewReflash()
    # print('model.insertRows(model.rowCount(),1)的返回值是：' + str(ret)）
def findRow(i):
    delrow=i.row()

def tableViewReflash():
    model.select()

if __name__=='__main__':
    app = QApplication(sys.argv)
    dataGrid=DataGridShow()
    dataGrid.show()
    initDatabase()
    model=QSqlTableModel()
    delrow=-1

    initModel(model)
    initView(dataGrid.tableView)

    dataGrid.tableView.clicked.connect(findRow)





    sys.exit(app.exec())