# from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys,time
from PyQt5 import QtCore

class AutoSignalSlot(QWidget):
    def __init__(self):
        super(AutoSignalSlot, self).__init__()
        self.okButton=QPushButton('ok',self)
        self.okButton.setObjectName('okButton')
        self.cancelButton=QPushButton('cancel',self)
        self.cancelButton.setObjectName('cancelButton')
        layout=QHBoxLayout()
        layout.addWidget(self.okButton)
        layout.addWidget(self.cancelButton)
        self.setLayout(layout)
        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):
        print('点击了ok按钮')

    @QtCore.pyqtSlot()
    def on_cancelButton_clicked(self):
        print('点击了cancel按钮')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AutoSignalSlot()
    main.show()

    sys.exit(app.exec_())


