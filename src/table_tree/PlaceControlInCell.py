import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class PlaceControlInCellDemo(QMainWindow):
    def __init__(self):
        super(PlaceControlInCellDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TableView演示案例')
        self.resize(600,400)

        tabelWidget=QTableWidget(self)
        tabelWidget.setRowCount(4)
        tabelWidget.setColumnCount(3)
        tabelWidget.setHorizontalHeaderLabels(['姓名','性别','年龄'])

        nameItem=QTableWidgetItem('adam')
        tabelWidget.setItem(0,0,nameItem)

        comboBox=QComboBox()
        comboBox.addItem('男')
        comboBox.addItem('女')
        #QSS
        comboBox.setStyleSheet('QComboBox(Margin:0px)')

        tabelWidget.setCellWidget(0,1,comboBox)

        modifyButton=QPushButton('修改')
        modifyButton.setDown(True)
        modifyButton.setStyleSheet('QPushButton(Margin:3px)')

        tabelWidget.setCellWidget(2,0,modifyButton)

        tabelWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tabelWidget.setSelectionBehavior(QAbstractItemView.SelectRows)




        self.setCentralWidget(tabelWidget)






    def tabelViewclicked(self,index):
        print(type(index))

        # print(self.tableView.index




if __name__=='__main__':
    app=QApplication(sys.argv)
    main=PlaceControlInCellDemo()
    main.show()

    sys.exit(app.exec_())