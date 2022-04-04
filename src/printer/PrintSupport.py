

import sys

import PyQt5.QtPrintSupport
from PyQt5.QtCore import QMimeData
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import QPrinter

class PrintSupport(QWidget):
    def __init__(self):
        super(PrintSupport, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('打印机演示案例')
        self.resize(800,500)

        layout=QVBoxLayout()

        self.button=QPushButton('print')
        self.button.clicked.connect(self.print)
        layout.addWidget(self.button)

        self.editor=QTextEdit()
        self.editor.setText('askljfajsf')
        layout.addWidget(self.editor)

        self.setLayout(layout)


        # QWidget * widget = new QWidget();
        # setCentralWidget(widget);
        # centralWidget()->setLayout(vlayout);

    def print(self):
        printer=QPrinter()
        painter=QPainter()
        painter.begin(printer)
        screen=self.textEdit.grab()
        painter.drawPixmap(50,50,screen)
        painter.end()
        print('print')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PrintSupport()
    main.show()

    sys.exit(QApplication.exec_())
