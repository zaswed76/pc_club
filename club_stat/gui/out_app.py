import os
import sys
from PyQt5 import QtWidgets, uic

root = os.path.join(os.path.dirname(__file__))
ui_pth = os.path.join(root, "ui/out_form.ui")

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.form = uic.loadUi(ui_pth, self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())