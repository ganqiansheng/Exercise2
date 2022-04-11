from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, time


class BasicQSS(QWidget):
    signalResize = pyqtSignal(int, int)

    def __init__(self):
        super(BasicQSS, self).__init__()
        self.setWindowTitle('QSS应用')
        self.resize(200, 50)

        btn1 = QPushButton('按钮1', self)
        btn2 = QPushButton('按钮2', self)
        btn3 = QPushButton('按钮3', self)
        btn4 = QPushButton('按钮4', self)

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = BasicQSS()
    qssStyle = '''
        QPushButton[name='btn2']{
            background-color:gray;
            color:yellow;
            height:120;
            font-size:48;
        }
        QPushButton[name='btn3']{
            background-color:blue;
            color:red;
            height:30;
            font-size:18;
        }
    '''
    main.setStyleSheet(qssStyle)
    main.show()

    sys.exit(app.exec_())
