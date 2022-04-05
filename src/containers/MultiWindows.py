import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *


class MultiWindows(QMainWindow):
    count = 0

    def __init__(self):
        super(MultiWindows, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('堆栈窗口控件演示案例')
        self.resize(800, 600)

        layout = QHBoxLayout()
        btnNew = QPushButton('new')
        btnNew.clicked.connect(lambda: (self.btnwindowaction(btnNew.text())))
        btnCascade = QPushButton('cascade')
        btnCascade.clicked.connect(lambda: (self.btnwindowaction(btnCascade.text())))
        btnTiled = QPushButton('Tiled')
        btnTiled.clicked.connect(lambda: (self.btnwindowaction(btnTiled.text())))

        layout.addWidget(btnNew)
        layout.addWidget(btnCascade)
        layout.addWidget(btnTiled)

        self.mdi = QMdiArea()
        bar = QMenuBar(self)

        file = bar.addMenu('File')

        file.addAction('New')
        file.addAction('cascade')
        file.addAction('Tiled')

        file.triggered.connect(self.windowaction)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layout)
        mainLayout.addWidget(self.mdi)

        # self.setLayout(mainLayout)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(mainLayout)

        # QWidget * widget = new QWidget();
        # setCentralWidget(widget);
        # centralWidget()->setLayout(vlayout);

    def btnwindowaction(self, text):
        if text== 'new':
            MultiWindows.count = MultiWindows.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle('子窗口' + str(MultiWindows.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        elif text == 'cascade':
            self.mdi.cascadeSubWindows()
        elif text == 'Tiled':
            self.mdi.tileSubWindows()

    def windowaction(self, checked):
        if checked.text() == 'New':
            MultiWindows.count = MultiWindows.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle('子窗口' + str(MultiWindows.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        elif checked.text() == 'cascade':
            self.mdi.cascadeSubWindows()
        elif checked.text() == 'Tiled':
            self.mdi.tileSubWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MultiWindows()
    main.show()

    sys.exit(app.exec_())
