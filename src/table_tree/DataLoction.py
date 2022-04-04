import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DataLoctionDemo(QWidget):
    def __init__(self):
        super(DataLoctionDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TableView演示案例')
        self.resize(600,800)

        layout=QVBoxLayout(self)
        tableWidget=QTableWidget(self)
        tableWidget.resize(550,750)
        tableWidget.setRowCount(40)
        tableWidget.setColumnCount(4)
        tableWidget.setHorizontalHeaderLabels(['第1列','第2列','第3列','第4列'])
        layout.addWidget(tableWidget)

        for i in range(40):
            for j in range(4):
                tableWidgetItem='(%d,%d)'%(i,j)
                tableWidget.setItem(i,j,QTableWidgetItem(tableWidgetItem))

        self.setLayout(layout)

        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        text='(1'
        items=tableWidget.findItems(text,Qt.MatchStartsWith)
        print(items)
        if len(items)>0:
            for item in items:
                item.setBackground(QBrush(QColor(0,255,0)))
                if item.column()==0:
                    item.setForeground((QBrush(QColor(255,0,0))))
                elif item.column()==1:
                    item.setForeground((QBrush(QColor(0,255,0))))
                elif item.column()==2:
                    item.setForeground((QBrush(QColor(0,255,255))))
                else:
                    item.setForeground((QBrush(QColor(255, 0, 255))))
                item.setFont(QFont('微软雅黑',20))
                row=item.row()
                tableWidget.verticalScrollBar().setSliderPosition(row)
                print(item.row())
                print(item.column())




        # tableWidget.resizeRowToContents(0)
        # tableWidget.resizeColumnToContents(0)
        # tableWidget.resizeColumnToContents(1)
        # tableWidget.resizeColumnToContents(2)

        # Custom = 2
        # Fixed = 2
        # Interactive = 0
        # ResizeToContents = 3
        # Stretch = 1

        # tableWidget.horizontalHeader().setVisible(True)

        # tableWidget.setShowGrid(False)





    def tabelViewclicked(self,index):
        print(type(index))

        # print(self.tableView.index




if __name__=='__main__':
    app=QApplication(sys.argv)
    main=DataLoctionDemo()
    main.show()

    sys.exit(app.exec_())