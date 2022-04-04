import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import QPrinter,QPageSetupDialog,QPrintDialog

class PrintDialog(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('打印对话框程序演示')
        self.resize(600,400)

        self.printer=QPrinter()

        layout=QFormLayout()

        self.editor=QTextEdit()
        self.editor.setText('需要打印的内容示例')
        # editor.setText(editor.toPlainText()+'   '+str(layout.geometry().x())+'   '+str(layout.geometry().height()))

        layoutRight=QVBoxLayout()

        btnOpenFile=QPushButton()
        btnOpenFile.setText('打开文件')
        btnOpenFile.clicked.connect(self.OpenFile)

        btnPageSet=QPushButton()
        btnPageSet.setText('页面设置')
        btnPageSet.clicked.connect(self.PageSetting)

        btnPrinterSet=QPushButton()
        btnPrinterSet.setText('打印机设置')
        btnPrinterSet.clicked.connect(self.PrinterSetting)

        layoutRight.addWidget(btnOpenFile)
        layoutRight.addWidget(btnPageSet)
        layoutRight.addWidget(btnPrinterSet)

        layout.addRow(self.editor,layoutRight)

        self.setLayout(layout)

    def OpenFile(self):
        fname=QFileDialog.getOpenFileName(self,'打开文本文件','.')
        print(fname[0])
        if fname[0]:
            with open(fname[0],encoding='utf-8',mode='r',errors='ignore') as f:
                self.editor.setText(f.read())
    def PageSetting(self):
        pageSettinDialog=QPageSetupDialog(self.printer,self)
        pageSettinDialog.exec()
    def PrinterSetting(self):
        printerDialog=QPrintDialog(self.printer,self)
        if QDialog.accepted==printerDialog.exec():
            self.editor.print(self.printer)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=PrintDialog()
    main.show()

    sys.exit(app.exec_())
