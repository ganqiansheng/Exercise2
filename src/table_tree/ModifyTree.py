import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

class ModifyTreeDemo(QWidget):
    def __init__(self):
        super(ModifyTreeDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('树控件单击响应演示案例')
        self.resize(600,400)

        operatorLayout=QHBoxLayout()

        addBtn=QPushButton('添加节点')
        updateBtn=QPushButton('修改节点')
        deleteBtn=QPushButton('删除节点')

        operatorLayout.addWidget(addBtn)
        operatorLayout.addWidget(updateBtn)
        operatorLayout.addWidget(deleteBtn)

        addBtn.clicked.connect(self.addNode)
        updateBtn.clicked.connect(self.updateNode)
        deleteBtn.clicked.connect(self.deleteNode)


        self.tree=QTreeWidget()
        self.tree.setColumnCount(2)
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

        self.tree.clicked.connect(self.onTreeClicked)

        self.tree.expandAll()

        # self.tree.setAttribute(Qt.WA_TransparentForMouseEvents,True)

        mainLayout=QVBoxLayout()
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tree)
        self.setLayout(mainLayout)

    def onTreeClicked(self,index):
        item=self.tree.currentItem()
        print(index.row())
        print('key=%s,value=%s'%(item.text(0),item.text(1)))

    def addNode(self):
        print('addNode')
        item=(self.tree.currentItem() or self.tree.invisibleRootItem())
        node=QTreeWidgetItem(item)
        node.setText(0,'新节点')
        node.setText(1,'新值')


    def updateNode(self):
        print('updateNode')
        item=self.tree.currentItem()
        item.setText(0,'新节点')
        item.setText(1,'新值')
    def deleteNode(self):
        print('deleteNode')
        root=self.tree.invisibleRootItem()
        item = self.tree.currentItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ModifyTreeDemo()
    main.show()

    sys.exit(app.exec_())

    '''
    ui->radioButton->setAttribute(Qt::WA_TransparentForMouseEvents, true);


    '''