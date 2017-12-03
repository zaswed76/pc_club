import os
import sys
from PyQt5 import QtWidgets, uic, QtGui

root = os.path.join(os.path.dirname(__file__))
ui_pth = os.path.join(root, "ui/itstat.ui")



class ItStat(QtWidgets.QMainWindow):
    def __init__(self, icon_dir):
        super().__init__()
        self.icon_dir = icon_dir
        self.center = QtWidgets.QFrame()
        self.setCentralWidget(self.center)
        self.form = uic.loadUi(ui_pth, self.center)

    def set_menu(self):
        icon_path = os.path.join(self.icon_dir, 'exit.png')
        exitAction = QtWidgets.QAction(QtGui.QIcon(icon_path), '&Exit', self)
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exit)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

    def set_version(self, version_text):
        self.form.label_version.setText(version_text)

    def set_adr_project(self, adr_text):
        t = '''<a href={adr}>website</a>'''.format(adr=adr_text)
        self.form.label_site.setText(t)

    def exit(self):
        QtWidgets.qApp.quit()


    def set_tray_icon(self):
        self.tray_icon = QtWidgets.QSystemTrayIcon()
        self.tray_icon.setIcon(QtGui.QIcon(os.path.join(self.icon_dir, 'tray.png')))
        show_action = QtWidgets.QAction("Show", self)

        hide_action = QtWidgets.QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)

        tray_menu = QtWidgets.QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def closeEvent(self, event):
        pass








if __name__ == '__main__':
    UI_DIR = "../club_stat/gui/ui"
    ui_pth = r"C:\Users\Cassa\Desktop\Serg\project\pc_club\club_stat\gui\ui\itstat.ui"
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = ItStat()
    main.show()
    sys.exit(app.exec_())