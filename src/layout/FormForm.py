import os
import sys
from PyQt5.QtCore import QUrl, QObject, pyqtSlot, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtGui import *

class FormFormDemo(QWidget):
    def __init__(self):
        super(FormFormDemo, self).__init__()
        self.setWindowTitle('表单设计')
        self.resize(350,300)

        titleLabel=QLabel('标题')
        authorLabel=QLabel('作者')
        contentLabel=QLabel('内容')

        titleLineEdit=QLineEdit()
        authorLineEdit=QLineEdit()
        contentTextEdit=QTextEdit()
        contentTextEdit.setText(str(contentTextEdit.width())+ '  '+str(contentTextEdit.height()))

        formLayout=QFormLayout()
        formLayout.setSpacing(10)
        self.setLayout(formLayout)

        formLayout.addRow(titleLabel,titleLineEdit)
        formLayout.addRow(authorLabel,authorLineEdit)
        formLayout.addRow(contentLabel,contentTextEdit)




if __name__=='__main__':
    app=QApplication(sys.argv)
    main=FormFormDemo()
    main.show()

    sys.exit(app.exec_())




