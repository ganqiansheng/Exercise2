from PyQt5.QtCore import QObject
from PyQt5.QtCore import *
class MyTypeSignal(QObject):
    sendmsg = pyqtSignal(str)

    sendmsg1 = pyqtSignal(str,int,int)

    sendmsg2 =pyqtSignal(str,int)
    def run(self):
        self.sendmsg.emit('Hello World')

        send.sendmsg1.emit('Hello World',4,3)

        send.sendmsg2.emit('hello World',-10)

class MySlot(QObject):
    def get(self,msg):
        print('信息：'+msg)

    def get1(self,msg,a,b):
        print('信息：'+msg+'  '+str(a)+'  '+str(b))


    def get2(self, msg, a):
        print('信息：' + msg + '  ' + str(a))


if __name__=='__main__':
    send =MyTypeSignal()
    slot = MySlot()

    send.sendmsg.connect(slot.get)

    send.sendmsg1.connect(slot.get1)

    send.sendmsg2.connect(slot.get2)

    send.run()

