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
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重'])
        layout.addWidget(self.tableWidget)

        newItem = QTableWidgetItem('jick')
        self.tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem('160')
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
        self.tableWidget.setItem(2, 1, newItem)
        newItem = QTableWidgetItem('154')
        self.tableWidget.setItem(2, 2, newItem)

        button = QPushButton('排序')
        button.clicked.connect(self.Sort)
        layout.addWidget(button)

        self.orderType = Qt.DescendingOrder

        self.setLayout(layout)

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
