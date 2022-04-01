#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QFormLayout, QTextEdit
from PyQt5 import QtCore, QtGui




class WidgetGeometry(QWidget):
    def __init__(self, parent=None):
        super(WidgetGeometry, self).__init__(parent)
        self.resize(1366, 768)
        self.move(200, 100)

        self.setWindowIcon(QtGui.QIcon('images/ICO/telephone.ICO'))

        self.formLayoutWidget = QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 1024, 500))
        self.formLayoutWidget.setObjectName('formLayoutWidget')
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignHCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignHCenter)
        self.formLayout.setContentsMargins(2, 2, 2, 2)
        self.formLayout.setObjectName('formLayout')

        # 在栅格布局中增加第一个按钮
        self.widgetbutton = QPushButton(self.formLayoutWidget)
        self.widgetbutton.setText('显示1')
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.widgetbutton)
        self.widgetbutton.clicked.connect(self.onClickwidgetButton)
        # 在栅格布局中增加第一个文本输入框
        self.widgetTextEdit = QTextEdit(self.formLayoutWidget)
        self.widgetTextEdit.clear()
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.widgetTextEdit)

        # 在栅格布局中增加第二个按钮
        self.widgetgeometrybutton = QPushButton(self.formLayoutWidget)
        self.widgetgeometrybutton.setText('显示2')
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.widgetgeometrybutton)
        self.widgetgeometrybutton.clicked.connect(self.onClickwidgetgeometrybutton)
        # 在栅格布局中增加第二个文本输入框
        self.widgetgeometryTextEdit = QTextEdit(self.formLayoutWidget)
        self.widgetgeometryTextEdit.clear()
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.widgetgeometryTextEdit)

        # 在栅格布局中增加第三个按钮
        self.widgetframegeometrybutton = QPushButton(self.formLayoutWidget)
        self.widgetframegeometrybutton.setText('显示3')
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.widgetframegeometrybutton)
        self.widgetframegeometrybutton.clicked.connect(self.onClickwidgetframegeometrybutton)
        # 在栅格布局中增加第三个文本输入框
        self.widgetframegeometryTextEdit = QTextEdit(self.formLayoutWidget)
        self.widgetframegeometryTextEdit.clear()
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.widgetframegeometryTextEdit)

        # self.widgetgeometrybutton=QPushButton('显示widget.geometry.x/y/width/height')
        # self.widgetgeometrybutton.clicked.connect(self.onClickwidgetgeometrybutton)
        # self.widgetframegeometrybutton=QPushButton('显示widget.framegeometry.x/y/width/height')
        # self.widgetframegeometrybutton.clicked.connect(self.onClickwidgetframegeometrybutton)
        #
        # self.quitbutton=QPushButton('退出应用程序')
        # self.quitbutton.clicked.connect(self.onClickQuitButton)

        # self.centralwidget.setObjectName("centralwidget")
        # self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        # self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 50, 161, 81))
        # self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        # self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)

        # layout=QVBoxLayout()
        # layout.addWidget(self.widgetbutton)
        # layout.addWidget(self.widgetgeometrybutton)
        # layout.addWidget(self.widgetframegeometrybutton)
        # layout.addWidget(self.quitbutton)

        # mainFrame=s
        # mainFrame.setLayout(layout)
        # self.setLayout(layout)

    # 显示widget.x/y/width/height
    def onClickwidgetButton(self):
        print('widget.x=%d' % self.x())
        print('widget.y=%d' % self.y())
        print('widget.width=%d' % self.width())
        print('widget.height=%d' % self.height())
        self.widgetTextEdit.setText(
            'widget.x=%d' % self.x() + '\n' + 'widget.y=%d' % self.y() + '\n' + 'widget.width=%d' % self.width() + '\n' + 'widget.height=%d' % self.height())

    # 显示widget.geometry.x/y/width/height
    def onClickwidgetgeometrybutton(self):
        print('widget.geometry().x=%d' % self.geometry().x())
        print('widget.geometry().y=%d' % self.geometry().y())
        print('widget.geometry().width=%d' % self.geometry().width())
        print('widget.geometry().height=%d' % self.geometry().height())
        self.widgetgeometryTextEdit.setText(
            'widget.geometry().x=%d' % self.geometry().x() + '\n' + 'widget.geometry().y=%d' % self.geometry().y() + '\n' + 'widget.geometry().width=%d' % self.geometry().width() + '\n' + 'widget.geometry().height=%d' % self.geometry().height())

    # 显示widget.framegeometry.x/y/width/height
    def onClickwidgetframegeometrybutton(self):
        print('widget.frameGeometry().x=%d' % self.frameGeometry().x())
        print('widget.frameGeometry().y=%d' % self.frameGeometry().y())
        print('widget.frameGeometry().width=%d' % self.frameGeometry().width())
        print('widget.frameGeometry().height=%d' % self.frameGeometry().height())
        self.widgetframegeometryTextEdit.setText(
            'widget.frameGeometry().x=%d' % self.frameGeometry().x() + '\n' + 'widget.frameGeometry().y=%d' % self.frameGeometry().y() + '\n' + 'widget.frameGeometry().width=%d' % self.frameGeometry().width() + '\n' + 'widget.frameGeometry().height=%d' % self.frameGeometry().height())

    # 退出应用程序
    def onClickQuitButton(self):
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wedgit = WidgetGeometry()
    wedgit.setWindowTitle('用栅格布局组合多个命令按钮')
    wedgit.show()

    sys.exit(QApplication.exec_())
