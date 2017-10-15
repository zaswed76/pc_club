
import sys
from PyQt5 import QtWidgets, QtCore

class Wind(QtWidgets.QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.Tool)
        self.setGeometry(300, 300, 250, 150)

    def close_window(self):
        self.close()
        quit()

    def keyPressEvent(self, e):
        if int(e.modifiers()) == (QtCore.Qt.ControlModifier +
                                      QtCore.Qt.AltModifier +
                                      QtCore.Qt.ShiftModifier):
            if e.key() == QtCore.Qt.Key_Q:
                self.close_window()


app = QtWidgets.QApplication(sys.argv)
icon = Wind()
icon.show()
sys.exit(app.exec_())