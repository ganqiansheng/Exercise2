import math
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
import math


class MyComboBox(QComboBox):
    def __init__(self):
        super(MyComboBox, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasText():
            e.accept()
        else:
            e.egnore()

    def dropEvent(self, e):
        self.addItem(e.mimeData().text())


class DragDropDemo(QWidget):
    def __init__(self):
        super(DragDropDemo, self).__init__()
        layout = QFormLayout()
        layout.addRow(QLabel('请将左侧的文本拖动到右侧的下拉列表中'))
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)
        combo = MyComboBox()
        layout.addRow(lineEdit, combo)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DragDropDemo()
    main.show()

    sys.exit(QApplication.exec_())
