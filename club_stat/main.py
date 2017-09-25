import os
import sys

import collections
import time, datetime
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time
from club_stat import webdriver, config, club
from club_stat.sql import sql_keeper

from club_stat.gui.itstat import ItStat

adr = "http://adminold.itland.enes.tech/index.php/map"

ROOT = os.path.join(os.path.dirname(__file__))
CSS_STYLE = os.path.join(ROOT, "css/style.css")
DATA_DIR = os.path.join(ROOT, "data")
DATA_FILE = os.path.join(DATA_DIR, "data.db")
ICON_DIR = os.path.join(ROOT, "resource/icons")

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

class Worker(QObject):
    finished = pyqtSignal()
    intReady = pyqtSignal(int)


    @pyqtSlot()
    def procCounter(self): # A slot takes no params
        for i in range(1, 100):
            time.sleep(1)
            self.intReady.emit(i)

        self.finished.emit()

class Main:
    def __init__(self):
        QtCore.qDebug('something informative')
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(open(CSS_STYLE, "r").read())
        self.gui = ItStat(ICON_DIR)
        self.gui.closeEvent = self.closeEvent
        self.gui.show()
        self.gui.set_tray_icon()
        self.gui.set_menu()
        self.clubs = club.Clubs()
        self.clubs["les"] = club.Club(club.Club.LES, club.Statistics())
        self.gui.form.start.clicked.connect(self.start)
        self.gui.form.stop.clicked.connect(self.stop)
        self.gui.form.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gui.statusBar()
        sys.exit(app.exec_())

    def init_thread(self):
        self.obj = Worker()  # no parent!
        self.thread = QThread()  # no parent!

        self.obj.intReady.connect(self.onIntReady)
        self.obj.moveToThread(self.thread)
        self.obj.finished.connect(self.thread.quit)
        self.thread.started.connect(self.obj.procCounter)




    def write_data(self):
        self.keeper.write()

    def read_data(self):
        stat = collections.OrderedDict()
        stat_names = ["load", "taken", "free", "guest",
                     "resident", "admin", "workers", "school"]


        self.web.select_club("4")
        time.sleep(1)
        date_time = datetime.datetime.now()
        date = date_time.date()
        try:
            for opt in stat_names:
                stat[opt] = self.web.get_data(opt)
        except Exception as er:
            print(er)
            raise Exception(er)

        seq = [date, date_time, self.clubs["les"].field_name]
        seq.extend(stat.values())
        seq = tuple(seq)

        self.keeper.add_line(sql_keeper.ins_club_stat(), seq)
        self.keeper.commit()



    def start(self):
        adr = self.gui.form.adress.text()
        login_id = 'enter_login'
        password_id = 'enter_password'
        submit_name = 'but_m'
        login = self.gui.form.login.text()
        password = self.gui.form.password.text()
        self.web = webdriver.WebDriver(adr, webdriver.WebDriver.Chrome)
        self.gui.statusBar().showMessage('открыл браузер')
        self.web.log_in(login_id, password_id, submit_name,
                        login, password)
        self.gui.statusBar().showMessage('залогинился')

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.read_data)
        self.timer.start(1000 * 60)
        self.keeper = sql_keeper.Keeper(DATA_FILE)
        self.keeper.open_connect()
        self.keeper.open_cursor()
        self.keeper.create_table(sql_keeper.table())



    def stop(self):
        try:
            self.timer.stop()
            self.keeper.close()
        except AttributeError as er:
            print(er)

    def closeEvent(self, event):
        event.ignore()
        self.gui.hide()
        self.gui.tray_icon.showMessage(
            "Tray Program",
            "Application was minimized to Tray",
            QtWidgets.QSystemTrayIcon.Information, 2000)


if __name__ == '__main__':
    Main()