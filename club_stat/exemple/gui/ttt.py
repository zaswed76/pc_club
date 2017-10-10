

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5 import QtGui


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

class Communicate(QObject):
    run_signal = pyqtSignal()

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.btn = QtWidgets.QPushButton("click", self)
        self.btn.clicked.connect(self.show_dialog)

    def show_dialog(self):
        self.dialog = Dialog()
        self.dialog.btn1.c.run_signal.connect(self.slot)
        self.dialog.btn2.c.run_signal.connect(self.slot)


        self.dialog.show()

    def slot(self):
        obj = self.sender()
        print(obj.sender())


class BtnLab(QtWidgets.QLabel):
    signal = pyqtSignal()
    def __init__(self, text):
        super().__init__(text)
        self.c = Communicate()

        self.resize(50, 30)
        font = QtGui.QFont('Helvetica', 24, QtGui.QFont.Bold)
        self.setFont(font)

    def mousePressEvent(self, event):
        self.c.run_signal.emit()

    def go(self):
        print("go")




class Dialog(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)



        self.resize(300, 300)
        box = QtWidgets.QHBoxLayout(self)
        self.btn1 = BtnLab("1")
        self.btn1.setStyleSheet("background-color: green")

        self.btn2 = BtnLab("2")
        self.btn2.setStyleSheet("background-color: blue")

        box.addWidget(self.btn1)
        box.addWidget(self.btn2)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())