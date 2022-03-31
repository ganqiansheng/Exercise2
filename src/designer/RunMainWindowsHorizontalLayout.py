import sys
import MainWindowsHorizontalLayout
from  PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=='__main__':
    app=QApplication(sys.argv)
    mainHorizontalWindow=QMainWindow()
    uimainHorizontalWindow=MainWindowsHorizontalLayout.Ui_MainWindow()
    uimainHorizontalWindow.setupUi(mainHorizontalWindow)
    mainHorizontalWindow.show()
    sys.exit(app.exec_())
