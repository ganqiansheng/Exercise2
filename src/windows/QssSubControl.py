from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, time


class QSSSubControl(QWidget):
    def __init__(self):
        super(QSSSubControl, self).__init__()
        self.setWindowTitle('QSS子控件选择器')
        self.resize(320, 150)

        combo = QComboBox(self)
        combo.setObjectName('myComboBox')
        combo.addItem('windows')
        combo.addItem('linux')
        combo.addItem('mac os X')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSSSubControl()
    qssStyle = '''
        QComboBox#myComboBox::drop-down{
            image:url(./images/SolutionCover.png);
            height:60;
        }
    '''
    # qssStyle = '''
    #     QPushButton[name='btn2']{
    #         background-color:gray;
    #         color:yellow;
    #         height:120;
    #         font-size:48;
    #     }
    #     QPushButton[name='btn3']{
    #         background-color:blue;
    #         color:red;
    #         height:30;
    #         font-size:18;
    #     }
    # '''
    main.setStyleSheet(qssStyle)
    main.show()

    sys.exit(app.exec_())
