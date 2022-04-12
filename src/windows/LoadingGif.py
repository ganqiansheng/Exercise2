import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math


class LoadingGif(QWidget):
    def __init__(self):
        super(LoadingGif, self).__init__()
        self.setWindowTitle('绘制异形窗口')
        self.resize(300,200)
        self.label=QLabel(self)
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint)
        # self.setWindowState(Qt.WindowFullScreen)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        # self.movie = QMovie('./images/loading.gif')
        # self.movie.setBackgroundColor(Qt.red)
        # # self.movie.setFileName('./images/loading.gif')
        # self.label.setMovie(self.movie)
        # self.movie.start()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LoadingGif()
    qssStyle='''
        QLabel{
            border-image:url('images/dog.jpg');
            width:77;
            height:22;
        }
    '''
    main.setStyleSheet(qssStyle)

    main.show()

    sys.exit(app.exec_())
