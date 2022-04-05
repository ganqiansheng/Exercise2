import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

class BasicTreeWidgetDemo(QMainWindow):
    def __init__(self):
        super(BasicTreeWidgetDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('树控件演示案例')
        self.resize(600,400)
        self.tree=QTreeWidget()
        self.tree.setColumnCount(3)
        self.tree.setHeaderLabels(['key','value'])
        self.tree.setColumnWidth(0,200)
        self.tree.setColumnWidth(1,200)
        root=QTreeWidgetItem(self.tree)
        root.setText(0,'根节点')
        root.setIcon(0,QIcon('./editico/edit_group.ico'))

        child1=QTreeWidgetItem(root)
        child1.setText(0,'子节点1')
        child1.setText(1,'子节点1的数据')
        child1.setIcon(0,QIcon('./editico/editcopy.ico'))
        child1.setCheckState(0,Qt.Checked)

        child11=QTreeWidgetItem(child1)
        child11.setText(0,'孙节点')
        child11.setIcon(0,QIcon('./editico/editpaste.ico'))

        child2=QTreeWidgetItem(root)
        child2.setText(0,'子节点2')
        child2.setText(1,'子节点2的数据')
        child2.setIcon(0,QIcon('./editico/edit_user.ico'))
        child2.setCheckState(0,Qt.Checked)

        child21=QTreeWidgetItem(child2)
        child21.setText(0,'孙节点21')
        child2.setText(1,'子节点21的数据')

        self.tree.expandAll()






        self.setCentralWidget(self.tree)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = BasicTreeWidgetDemo()
    main.show()

    sys.exit(app.exec_())