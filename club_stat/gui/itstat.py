import os
import sys
from PyQt5 import QtWidgets, uic

root = os.path.join(os.path.dirname(__file__))
ui_pth = os.path.join(root, "ui/itstat.ui")


class ItStat(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.center = QtWidgets.QFrame()
        self.setCentralWidget(self.center)
        self.form = uic.loadUi(ui_pth, self.center)

    def closeEvent(self, *args, **kwargs):
        pass






if __name__ == '__main__':
    UI_DIR = "../club_stat/gui/ui"
    ui_pth = r"C:\Users\Cassa\Desktop\Serg\project\pc_club\club_stat\gui\ui\itstat.ui"
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = ItStat()
    main.show()
    sys.exit(app.exec_())