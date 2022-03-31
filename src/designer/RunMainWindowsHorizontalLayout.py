import sys
import MainWindowsHorizontalLayout
from  PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    uim=MainWindowsHorizontalLayout.Ui_MainWindow()
    uim.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
