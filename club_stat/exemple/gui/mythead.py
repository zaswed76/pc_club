


import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time

def qt_message_handler(mode, context, message):
    if mode == QtCore.QtInfoMsg:
        mode = 'INFO'
    elif mode == QtCore.QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCore.QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtCore.QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print('qt_message_handler: line: %d, func: %s(), file: %s' % (
          context.line, context.function, context.file))
    print('  %s: %s\n' % (mode, message))

QtCore.qInstallMessageHandler(qt_message_handler)

class Worker(QObject):
    finished = pyqtSignal()
    intReady = pyqtSignal(int)



    @pyqtSlot()
    def procCounter(self): # A slot takes no params
        for i in range(1, 100):
            time.sleep(1)
            self.intReady.emit(i)

        self.finished.emit()


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

        self.label = QtWidgets.QLabel("0", self)
        self.btn = QtWidgets.QPushButton("f", self)
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.finish)


        self.obj = Worker()  # no parent!
        self.thread = QThread()  # no parent!

        self.obj.intReady.connect(self.onIntReady)
        self.obj.moveToThread(self.thread)
        self.obj.finished.connect(self.thread.quit)
        self.thread.started.connect(self.obj.procCounter)
        self.thread.start()

    def onIntReady(self, i):
        self.label.setText(str(i))

    def finish(self):
        print("f")
        self.thread.quit()
        # self.thread.wait()


if __name__ == '__main__':
    QtCore.qDebug('something informative')
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())