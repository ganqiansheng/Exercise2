from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys,time

class BackendTread(QThread):
    update_date=pyqtSignal(str)

    def run(self):
        while True:
            data=QDateTime.currentDateTime()
            currentTime =data.toString('yyyy-MM-dd hh:mm:ss')
            self.update_date.emit(currentTime)
            time.sleep(1)

class ThreadUpdateUI(QDialog):
    def __init__(self):
        super(ThreadUpdateUI, self).__init__()
        self.setWindowTitle('多线程更新时间')
        self.resize(400,300)

        self.input=QLineEdit(self)
        self.input.resize(400,300)
        self.input.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        self.input.setFont(QFont('Arial',40))
        self.initUI()

    def initUI(self):
        self.thread=BackendTread()
        self.thread.update_date.connect(self.updateDate)
        self.thread.start()

    def updateDate(self,date):
        self.input.setText(date)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ThreadUpdateUI()
    main.show()

    sys.exit(app.exec_())




