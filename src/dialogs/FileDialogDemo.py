import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDir
from PyQt5.QtGui import *


class QFontDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('字体对话框演示')
        self.resize(300, 400)

        layout = QVBoxLayout()
        self.buttonPic = QPushButton('设置图像')
        self.buttonPic.clicked.connect(self.LoadPic)
        self.labelPic = QLabel()
        layout.addWidget(self.buttonPic)
        layout.addWidget(self.labelPic)

        self.buttonText = QPushButton('设置文本')
        self.buttonText.clicked.connect(self.LoadText)
        self.texteditText = QTextEdit()
        layout.addWidget(self.buttonText)
        layout.addWidget(self.texteditText)
        self.setLayout(layout)

    def LoadPic(self):
        fname, ok = QFileDialog.getOpenFileName(self, '打开文件', '.', '图像文件(*.jpg *.PNG)')
        if ok:
            self.labelPic.setPixmap(QPixmap(fname))

    def LoadText(self):
        # fname,_=QFileDialog.getOpenFileName(self,'打开文件','.','文本文件(*.py *.txt)')
        # with open(fname,encoding='utf-8',mode='r') as f:
        #     data=f.read()
        #     self.texteditText.setText(data)
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            filename = filenames[0]
            with open(filename, encoding='utf-8', mode='r') as f:
                data = f.read()
                self.texteditText.setText(filename + '\n' + data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.show()

    sys.exit(QApplication.exec_())
