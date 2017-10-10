
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QHBoxLayout

class Communicate(QObject):
    run = pyqtSignal()

class Example(QLabel):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.run)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.run.emit()

    def run(self):
        print("run")

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        box = QHBoxLayout(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    sys.exit(app.exec_())