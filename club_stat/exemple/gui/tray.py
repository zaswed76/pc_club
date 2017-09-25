

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class Widget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.tray_icon = QtWidgets.QSystemTrayIcon()
        # r = self.icon.isSystemTrayAvailable()

        self.tray_icon.setIcon(QtGui.QIcon('tray.png'))
        self.tray_icon.show()
        self.center = QtWidgets.QFrame()
        self.setCentralWidget(self.center)
        self.cl_btn = QtWidgets.QPushButton("close", self)
        self.cl_btn.clicked.connect(self.close_wind)



        show_action = QtWidgets.QAction("Show", self)
        quit_action = QtWidgets.QAction("Exit", self)
        hide_action = QtWidgets.QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(QtWidgets.qApp.quit)
        tray_menu = QtWidgets.QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def close_wind(self):
        self.close()

    def closeEvent(self, event):
            event.ignore()
            self.hide()
            self.tray_icon.showMessage(
                "Tray Program",
                "Application was minimized to Tray",
                QtWidgets.QSystemTrayIcon.Information,
                2000
            )

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()



    main.show()
    sys.exit(app.exec_())




