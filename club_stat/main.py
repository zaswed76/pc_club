import sys
from PyQt5 import QtWidgets



from club_stat.gui.itstat import ItStat

adr = "http://adminold.itland.enes.tech/index.php/map"




def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open('css/style.css', "r").read())
    gui = ItStat()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()