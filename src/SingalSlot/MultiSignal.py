from PyQt5.QtCore import *
class MultiSingal(QObject):
    signal1 = pyqtSignal()
    signal2=pyqtSignal(int)
    signal3=pyqtSignal(int,str)
    signal4=pyqtSignal(list)
    signal5=pyqtSignal(dict)
    signal6=pyqtSignal([int,str],[int])  #重载版本的信号

    def __init__(self):
        super(MultiSingal, self).__init__()
        self.signal1.connect(self.signalCall1)
        self.signal2.connect(self.signalCall2)
        self.signal3.connect(self.signalCall3)
        self.signal4.connect(self.signalCall4)
        self.signal5.connect(self.signalCall5)
        self.signal6[int].connect(self.signalCall6Overload)
        self.signal6[int,str].connect(self.signalCall6)

        self.signal1.emit()
        self.signal2.emit(10)
        self.signal3.emit(10,'Hello world')
        self.signal4.emit([1,2,3,4,5])
        self.signal5.emit({'name':'zhangfei','age':30})
        self.signal6.emit(122,'hello world')
        self.signal6[int,str].emit(122,'hello world')
        self.signal6[int].emit(122)


    def signalCall1(self):
        print('signal emit')
    def signalCall2(self,val):
        print('signal emit,val:',val)
    def signalCall3(self,val,text):
        print('signal emit,val,text',val,text)
    def signalCall4(self,val):
        print('signal emit,val:',val)
    def signalCall5(self,val):
        print('signal emit,val:',val)
    def signalCall6(self,val,text):
        print('signal emit,val,text:',val,text)
    def signalCall6Overload(self,val):
        print('signal emit,val,text:',val)

if __name__=='__main__':
    multiSignal=MultiSingal()

