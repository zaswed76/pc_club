

 #!/usr/bin/python
from PyQt5.Qt import *
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.window()
    def window (self):
        b1 = QPushButton('1')
        b2 = QPushButton('2')
        b3 = QPushButton('3')
        b4 = QPushButton('4')
        frame = QFrame()
        grid=QGridLayout()
        b1.setFixedHeight(70)
        b2.setFixedHeight(70)
        grid.addWidget(b1, 0 ,0)
        grid.addWidget(b2, 0 ,1)
        grid.addWidget(b3, 1 ,0)
        grid.addWidget(b4, 1 ,1)
        # Здесь убирается, более нигде
        grid.setContentsMargins(0,0,0,0)
        grid.setSpacing(0)
        frame.setLayout(grid)
        frame.setStyleSheet("border:1px solid blue;")
        Hbox = QHBoxLayout()
        Hbox.setContentsMargins(0, 0, 0, 0)
        Hbox.addWidget(frame)
        self.setLayout(Hbox)
    def exit_app (self):
        self.close()
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())