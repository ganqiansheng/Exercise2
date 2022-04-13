import PyQt5.QtBluetooth
from PyQt5.QtSql import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys,os


class DataGrid(QWidget):
    def __init__(self):
        super(DataGrid, self).__init__()
        self.const()
        self.initUI()
        self.initDatabase()

    #     self.close.connect(self.dbClose)
    #
    # def dbClose(self):
    #     if self.db.open():
    #         self.db.close()

    # 常量定义
    def const(self):
        # 当前页
        self.currentPage = 0
        # 总页数
        self.totalPage = 0
        # 总记录数
        self.totalRecordCount = 0
        # 每页显示记录数
        self.pageRecordCount = 6

    def closeEvent(self, event):
        self.db.close()
    # 界面初始化
    def initUI(self):
        self.setWindowTitle('分页查询数据显示')
        self.resize(550, 400)
        self.initDatabase()

        # 建立三个区域，
        #   最上面为查询区， layoutQuery
        #   中间为数据展示区，layoutData
        #   下面为状态区 layoutStatus
        layoutQuery = QHBoxLayout()
        layoutData = QHBoxLayout()
        layoutStatus = QHBoxLayout()

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layoutQuery)
        mainLayout.addLayout(layoutData)
        mainLayout.addLayout(layoutStatus)

        # layoutQuery查询区中的控件
        self.buttonPrevPage = QPushButton('上一页')
        self.buttonNextPage = QPushButton('下一页')
        self.lableTo = QLabel('转到第')
        self.lineEditPage = QLineEdit()
        self.lineEditPage.setFixedWidth(40)
        self.labelPage = QLabel('页')
        self.buttonGo = QPushButton('Go')
        layoutQuery.addWidget(self.buttonPrevPage)
        layoutQuery.addWidget(self.buttonNextPage)
        layoutQuery.addWidget(QSplitter())
        layoutQuery.addWidget(self.lableTo)
        layoutQuery.addWidget(self.lineEditPage)
        layoutQuery.addWidget(self.labelPage)
        layoutQuery.addWidget(self.buttonGo)
        layoutQuery.addWidget(QSplitter())

        # layoutData数据区中的控件
        self.tableView = QTableView()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layoutData.addWidget(self.tableView)

        # layoutStatus状态区中的控件
        self.labelTotlePageNum = QLabel('总共5页')
        self.labelTotlePageNum.setFixedWidth(70)
        self.labelCurrentPage = QLabel('当前第5页')
        self.labelCurrentPage.setFixedWidth(70)
        self.labelTotleRecordNum = QLabel('总共5页')
        self.labelTotleRecordNum.setFixedWidth(70)
        layoutStatus.addWidget(self.labelTotlePageNum)
        layoutStatus.addWidget(self.labelCurrentPage)
        layoutStatus.addWidget(QSplitter())
        layoutStatus.addWidget(self.labelTotleRecordNum)

        self.setLayout(mainLayout)

        self.buttonPrevPage.clicked.connect(self.buttonPrevPageClick)
        self.buttonNextPage.clicked.connect(self.buttonNextPageClick)
        self.buttonGo.clicked.connect(lambda :self.goPage(self.lineEditPage.text()))

        # 初始化数据连接
        self.initDatabase()

        # 设置tableview数据显示
        self.setTableView()

    def setTableView(self):
        self.querymodel = QSqlQueryModel(self)
        self.currentPage = 1
        self.totleRecordCount = self.getTotleRecordCount()
        self.totlePageCount = self.getTotlePageCount()

        validator = QIntValidator(1,self.totlePageCount,self)
        self.lineEditPage.setValidator(validator)

        self.setOption()

        self.recordQuery()

        self.tableView.setModel(self.querymodel)
        self.db.close()

        # 设置表格头
        self.querymodel.setHeaderData(0, Qt.Horizontal, '编号')
        self.querymodel.setHeaderData(1, Qt.Horizontal, '姓名')
        self.querymodel.setHeaderData(2, Qt.Horizontal, '性别')
        self.querymodel.setHeaderData(3, Qt.Horizontal, '年龄')
        self.querymodel.setHeaderData(4, Qt.Horizontal, '院系')

    def setOption(self):
        self.setStatus()
        self.setbuttonEnable()

    def initDatabase(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        # print(os.getcwd()+'/db/database.db')
        self.db.setDatabaseName(os.getcwd()+'/db/database.db')
        if not self.db.open():
            return False

    def getTotleRecordCount(self):
        query = ('select * from student')
        self.querymodel.setQuery(query)
        rowCount = self.querymodel.rowCount()
        # print(rowCount)
        return rowCount

    def getTotlePageCount(self):
        if self.totleRecordCount % self.pageRecordCount == 0:
            pageCount = self.totleRecordCount // self.pageRecordCount
        else:
            pageCount = self.totleRecordCount // self.pageRecordCount + 1
        return pageCount

    def setStatus(self):
        self.labelTotlePageNum.setText('总共' + str(self.totlePageCount) + '页')
        self.labelCurrentPage.setText('当前' + str(self.currentPage) + '页')
        self.labelTotleRecordNum.setText('共' + str(self.totleRecordCount) + '条')

    def setbuttonEnable(self):
        if self.totlePageCount <= 1:
            self.buttonPrevPage.setEnabled(False)
            self.buttonNextPage.setEnabled(False)
        elif self.currentPage == 1:
            self.buttonPrevPage.setEnabled(False)
            self.buttonNextPage.setEnabled(True)
        elif self.currentPage == self.totlePageCount:
            self.buttonPrevPage.setEnabled(True)
            self.buttonNextPage.setEnabled(False)
        else:
            self.buttonPrevPage.setEnabled(True)
            self.buttonNextPage.setEnabled(True)

    def recordQuery(self):
        query = "select * from student limit %d,%d" % (
            ((self.currentPage - 1) * self.pageRecordCount), self.pageRecordCount)
        # print(query)
        self.querymodel.setQuery(query)

    def buttonPrevPageClick(self):
        self.currentPage -= 1
        self.recordQuery()
        self.setOption()

    def buttonNextPageClick(self):
        self.currentPage += 1
        self.recordQuery()
        self.setOption()

    def goPage(self,page):
        if page.strip()=='':
            QMessageBox.about(self,'提示','页码不能为空')

        elif int(page.strip())<=0:
            QMessageBox.about(self,'提示','页码不能为负数')

        elif int(page.strip())>self.totlePageCount:
            QMessageBox.about(self,'提示','页码超过总页数')
        else:
            self.currentPage=int(page.strip())
            self.recordQuery()
            self.setOption()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = DataGrid()
    form.show()

    sys.exit(app.exec())
