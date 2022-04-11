from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class WinSignal(QWidget):
    button_clicked_signal = pyqtSignal()

    def __init__(self):
        super(WinSignal, self).__init__()
        btn = QPushButton('关闭窗口', self)
        QMessageBox.about(self, '提示', '第一步')
        btn.clicked.connect(self.btn_clicked)
        self.button_clicked_signal.connect(self.btn_clicked)

    def btn_close(self):
        QMessageBox.about(self, '提示', '第二步')
        self.close()

    def btn_clicked(self):
        QMessageBox.about(self, '提示', '第一步')
        self.button_clicked_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WinSignal()
    main.show()

    sys.exit(app.exec_())
