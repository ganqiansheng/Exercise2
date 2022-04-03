

import sys

from PyQt5.QtCore import QMimeData
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class ClipBoard(QDialog):
    def __init__(self):
        super(ClipBoard, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('剪贴板演示案例')
        self.resize(600,400)

        gridLayout = QGridLayout()

        self.btnCopyText=QPushButton('复制文本')
        self.btnPasteText=QPushButton('粘贴文本')
        self.btnCopyHTML=QPushButton('复制HTML')
        self.btnPasteHTML=QPushButton('粘贴HTML')
        self.btnCopyImage=QPushButton('复制图像')
        self.btnPasteImage=QPushButton('粘贴图像')
        self.textEdit=QTextEdit('默认文本')
        self.imageLabel=QLabel()
        self.imageLabel.setPixmap(QPixmap('./images/small4.png'))

        gridLayout.addWidget(self.btnCopyText,0,0)
        gridLayout.addWidget(self.btnPasteText,1,0)
        gridLayout.addWidget(self.btnCopyHTML,0,1)
        gridLayout.addWidget(self.btnPasteHTML,1,1)
        gridLayout.addWidget(self.btnCopyImage,0,2)
        gridLayout.addWidget(self.btnPasteImage,1,2)

        self.btnCopyText.clicked.connect(self.CopyText)
        self.btnPasteText.clicked.connect(self.PasteText)
        self.btnCopyHTML.clicked.connect(self.CopyHTML)
        self.btnPasteHTML.clicked.connect(self.PasteHTML)
        self.btnCopyImage.clicked.connect(self.CopyImage)
        self.btnPasteImage.clicked.connect(self.PasteImage)


        gridLayout.addWidget(self.textEdit,2,0,2,1)
        gridLayout.addWidget(self.imageLabel,2,2)

        self.setLayout(gridLayout)
    #拷贝文本到剪贴板
    def CopyText(self):
        clipBoard = QApplication.clipboard()
        clipBoard.setText(self.textEdit.toPlainText())
    #粘贴文本到文本框
    def PasteText(self):
        self.textEdit.clear()
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setText('作为普通文本复制：\n'+QApplication.clipboard().text())

    def CopyHTML(self):
        mimeData=QMimeData()
        print(self.textEdit.acceptRichText())
        print(self.textEdit.toPlainText())
        print(self.textEdit.toHtml())
        clipBoard=QApplication.clipboard()
        if self.textEdit.acceptRichText() :
            clipBoard.setMimeData(self.textEdit.toHtml())
            QMessageBox.information(self, '消息', '复制到剪贴板成功', QMessageBox.Yes)
        else:
            QMessageBox.warning(self,'消息','复制对像不是一个HTML文本',QMessageBox.Yes)


    def PasteHTML(self):
        self.textEdit.clear()
        self.textEdit.setAcceptRichText(True)
        clipBoard = QApplication.clipboard()
        clipBoard.setText(self.textEdit.toHtml())

    def CopyImage(self):
        clipBoard = QApplication.clipboard()
        print(self.imageLabel.pixmap())
        clipBoard.setPixmap(self.imageLabel.pixmap())

    def PasteImage(self):
        # image=QImage(QApplication.clipboard().pixmap())
        # image.save('./images/9901.png')
        self.imageLabel.setPixmap(QApplication.clipboard().pixmap())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ClipBoard()
    main.show()

    sys.exit(QApplication.exec_())
