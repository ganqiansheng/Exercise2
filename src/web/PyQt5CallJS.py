import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView


class WebEngineView(QWidget):
    def __init__(self):
        super(WebEngineView, self).__init__()

        self.setWindowTitle('PyQt5与JavaScript交互演示案例')
        self.resize(1155, 730)
        self.move(50,50)

        self.layout=QVBoxLayout()
        self.browser=QWebEngineView()
        url=os.getcwd()+'/tt.html'
        self.browser.load(QUrl.fromLocalFile(url))

        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)

        button=QPushButton('设置全名')
        self.layout.addWidget(button)
        button.clicked.connect(self.fullname)

    def js_callback(self,result):
        print(result)

    def fullname(self):
        self.value='hello world'
        self.browser.page().runJavaScript('fullname("'+self.value+'");',self.js_callback)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WebEngineView()
    main.show()

    sys.exit(app.exec_())
