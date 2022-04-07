import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView



class WebEngineView(QMainWindow):
    def __init__(self):
        super(WebEngineView,self).__init__()

        self.setWindowTitle('web控件演示案例')
        self.resize(1355,730)

        self.browser = QWebEngineView()
        # self.browser.load(QUrl('https://geekori.com'))
        url=os.getcwd()+'/test.html'
        print(url)
        # url='http://www.ssssss.com.cn'
        self.browser.load(QUrl.fromLocalFile(url))

        self.setCentralWidget(self.browser)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WebEngineView()
    main.show()

    sys.exit(app.exec_())
