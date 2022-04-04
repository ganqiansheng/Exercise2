import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ListView(QWidget):
    def __init__(self):
        super(ListView, self).__init__()
        self.initUI()


    def initUI(self):
        self.resize(1000,800)

        listView=QListView()
        listView.resize(800,600)

        listModel=QStringListModel()
        self.list=['列表项1','列表项2','列表项3','列表项4','列表项5','列表项6','列表项7','列表项8']
        listModel.setStringList(self.list)

        listView.setModel(listModel)
        listView.clicked.connect(self.listClicked)


        layout=QVBoxLayout()
        layout.addWidget(listView)
        self.setLayout(layout)

    def listClicked(self,item):
        print(type(item))
        QMessageBox.information(self,'ListView',self.list[item.row()]+ '被选中')





if __name__=='__main__':
    app=QApplication(sys.argv)
    main=ListView()
    main.show()

    sys.exit(app.exec_())