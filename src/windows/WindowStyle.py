from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys,time

class WindowStyle(QWidget):
    def __init__(self):
        super(WindowStyle, self).__init__()
        self.setWindowTitle('设置窗口网格')
        # self.resize(300,50)
        horizontallayout=QHBoxLayout()
        self.styleLabel=QLabel('设置窗口风格:')
        self.styleComboBox=QComboBox()
        self.styleComboBox.addItems(QStyleFactory.keys())

        print(QApplication.style().objectName())
        index=self.styleComboBox.findText(QApplication.style().objectName(),Qt.MatchFixedString)

        self.styleComboBox.setCurrentIndex(index)

        self.styleComboBox.activated[str].connect(self.handleStyleChanged)

        horizontallayout.addWidget(self.styleLabel)
        horizontallayout.addWidget(self.styleComboBox)

        self.setLayout(horizontallayout)

    def handleStyleChanged(self,style):
        QApplication.setStyle(style)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WindowStyle()
    main.show()

    sys.exit(app.exec_())

