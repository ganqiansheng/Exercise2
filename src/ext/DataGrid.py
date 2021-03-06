import os.path
import sys

from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


def initializeMode(model):
    model.setTable('people')
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, Qt.Horizontal, 'ID')
    model.setHeaderData(1, Qt.Horizontal, '姓名')
    model.setHeaderData(2, Qt.Horizontal, '地址')


def createView(title, model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view


def findrow(i):
    delrow = i.row()
    print('del row=%s' % str(delrow))


def addrow():
    ret = model.insertRows(model.rowCount(), 1)
    print('insertRows=%s' % str(ret))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./db/database.db')
    model = QSqlTableModel()
    delrow = -1
    initializeMode(model)

    view = createView('展示数据', model)

    view.clicked.connect(findrow)

    dlg = QDialog()

    layout = QVBoxLayout()
    layout.addWidget(view)
    addBtn = QPushButton('添加一行')
    addBtn.clicked.connect(addrow)
    layout.addWidget(addBtn)

    delBtn = QPushButton('删除一行')
    delBtn.clicked.connect(lambda: model.removeRow(view.currentIndex().row()))
    layout.addWidget(delBtn)

    dlg.setLayout(layout)

    dlg.setWindowTitle('database demo')
    dlg.resize(500, 400)
    dlg.show()

    sys.exit(app.exec())
