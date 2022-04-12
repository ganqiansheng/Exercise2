import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math


class LabelButtonBackground(QWidget):
    def __init__(self):
        super(LabelButtonBackground, self).__init__()
        self.setWindowTitle('绘制异形窗口')
        self.resize(300,200)
        self.label1=QLabel(self)
        # self.label2=QLabel(self)
        button=QPushButton()
        # print(button.height())
        button.setMinimumHeight(48)
        button.setObjectName('button')
        # button.setGraphicsEffect(Qt.)
        qss='''
            QPushButton#button{
                border-radius:4px;
                background-image:url(./images/add.png)
            }
            #button:pressed{
                background-image:url(./images/addhover.png)
                
            }
            
            '''
        button.setStyleSheet(qss)
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint)
        # self.setWindowState(Qt.WindowFullScreen)
        # self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        # self.movie = QMovie('./images/loading.gif')
        # self.movie.setBackgroundColor(Qt.red)
        # # self.movie.setFileName('./images/loading.gif')
        # self.label.setMovie(self.movie)
        # self.movie.start()
        layout=QVBoxLayout()
        layout.addWidget(self.label1)
        # layout.addWidget(self.label2)
        layout.addWidget(button)
        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LabelButtonBackground()
    qssStyle='''
        QLabel{
            border-image:url('images/python.jpg');
            width:77;
            height:22;
        }
    '''
    main.setStyleSheet(qssStyle)

    main.show()

    sys.exit(app.exec_())
