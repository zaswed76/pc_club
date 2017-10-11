

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

class BtnLab(QtWidgets.QLabel):
    signal = pyqtSignal(str)
    def __init__(self, text, color, parent=None, *__args):
        super().__init__(*__args)
        self.color = color
        self.setStyleSheet("background-color: {}".format(color))

    def mousePressEvent(self, event):
        # генерируем сигнал
        self.signal.emit(self.color)


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.dialog = Dialog()
        # соединяем сигнал со слотом
        self.dialog.btn1.signal.connect(self.press_lb)
        self.dialog.btn2.signal.connect(self.press_lb)
        self.dialog.show()


    def press_lb(self, color):
        self.setStyleSheet("background-color: {}".format(color))




class Dialog(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        box = QtWidgets.QHBoxLayout(self)
        self.btn1 = BtnLab("1", "green")
        self.btn1.setStyleSheet("background-color: green")

        self.btn2 = BtnLab("2", "blue")
        self.btn2.setStyleSheet("background-color: blue")

        box.addWidget(self.btn1)
        box.addWidget(self.btn2)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())