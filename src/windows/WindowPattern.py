from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys,time

class WindowPattern(QMainWindow):
    def __init__(self):
        super(WindowPattern, self).__init__()
        self.setWindowTitle('设置窗口样式')
        self.resize(500,260)

        self.setWindowFlags(Qt.WindowMaximizeButtonHint|Qt.WindowStaysOnTopHint)
        self.setObjectName('MainWindow')
        self.setStyleSheet('#MainWindow{border-image:url(images/SolutionCover.png);}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WindowPattern()
    main.show()

    sys.exit(app.exec_())

