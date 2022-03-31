import sys
import MainWindowsVerticalLayout
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWindows=QMainWindow()
    ui=MainWindowsVerticalLayout.Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.show()
    sys.exit(app.exec_())