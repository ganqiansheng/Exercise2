import sys
import MultiLayout
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWindows=QMainWindow()
    ui=MultiLayout.Ui_Form()
    ui.setupUi(mainWindows)
    mainWindows.show()
    sys.exit(app.exec_())