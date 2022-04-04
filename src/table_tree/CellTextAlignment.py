import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ColumnSortDemo(QWidget):
    def __init__(self):
        super(ColumnSortDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TableView演示案例')
        self.resize(600, 800)

        layout = QVBoxLayout(self)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(550, 750)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setIconSize(QSize(50, 50))
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])
        layout.addWidget(self.tableWidget)

        newItem = QTableWidgetItem('jick')
        newItem.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem('男')
        newItem.setTextAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem('160')
        newItem.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.tableWidget.setItem(0, 2, newItem)
        newItem = QTableWidgetItem('adam')
        self.tableWidget.setItem(1, 0, newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(1, 1, newItem)
        newItem = QTableWidgetItem('139')
        self.tableWidget.setItem(1, 2, newItem)
        newItem = QTableWidgetItem('bob')
        self.tableWidget.setItem(2, 0, newItem)
        newItem = QTableWidgetItem('男')
        newItem.setFont(QFont('微软雅黑', 50))
        self.tableWidget.setItem(2, 1, newItem)
        newItem = QTableWidgetItem('154')
        self.tableWidget.setItem(2, 2, newItem)
        self.tableWidget.setRowHeight(3, 100)
        newItem = QTableWidgetItem(QIcon('./editico/editcopy.ico'), '复制')
        self.tableWidget.setItem(3, 0, newItem)

        # self.tableWidget.setSpan(0, 0, 3, 1)

        self.tableWidget.setRowHeight(2, 100)
        self.tableWidget.setColumnWidth(2, 200)

        button = QPushButton('排序')
        button.clicked.connect(self.Sort)
        layout.addWidget(button)

        self.orderType = Qt.DescendingOrder

        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.generateMemu)

        self.setLayout(layout)

    def generateMemu(self, pos):
        print(pos)
        for i in self.tableWidget.selectionModel().selection().indexes():
            rowNum = i.row()
        if rowNum < 4:
            menu = QMenu()
            item1 = menu.addAction('菜单项1')
            item2 = menu.addAction('菜单项2')
            item3 = menu.addAction('菜单项3')
            screenPos=self.tableWidget.mapToGlobal(pos)
            action=menu.exec_(screenPos)

            if action==item1:
                print('选择了第1个菜单项',self.tableWidget.item(rowNum,0).text(),
                                       self.tableWidget.item(rowNum, 1).text(),
                                        self.tableWidget.item(rowNum, 2).text())
            elif action==item2:
                print('选择了第2个菜单项',self.tableWidget.item(rowNum,0).text(),
                                       self.tableWidget.item(rowNum, 1).text(),
                                        self.tableWidget.item(rowNum, 2).text())
            elif action==item3:
                print('选择了第3个菜单项',self.tableWidget.item(rowNum,0).text(),
                                       self.tableWidget.item(rowNum, 1).text(),
                                        self.tableWidget.item(rowNum, 2).text())
            else:
                return


    def Sort(self):
        if self.orderType == Qt.DescendingOrder:
            self.orderType = Qt.AscendingOrder
        else:
            self.orderType = Qt.DescendingOrder
        self.tableWidget.sortItems(2, self.orderType)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ColumnSortDemo()
    main.show()

    sys.exit(app.exec_())
