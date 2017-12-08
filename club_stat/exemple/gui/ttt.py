

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





 # -*- coding: UTF-8 -*-
import sys
import time
from PyQt5 import QtWidgets
def on_clicked():

    button.setEnabled(False)
    QtWidgets.QApplication.processEvents()
    for i in range(1000000000):
        print(i**3)
        # time.sleep(1)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    button = QtWidgets.QPushButton('Button')
    button.clicked.connect(on_clicked)
    box = QtWidgets.QHBoxLayout()
    box.addWidget(button)
    window.setLayout(box)
    window.show()
    sys.exit(app.exec_())
