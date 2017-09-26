import os
import sys

import collections
import time, datetime
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time
import selenium
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

class Web(QObject):
    finished = pyqtSignal()
    str_web_process = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.running = False
        self.clubs = club.Clubs()
        self.clubs["les"] = club.Club(club.Club.LES, club.Statistics())

    # def __getattr__(self, attr):
    #     print("Yep, I know", attr)


    def read_data(self):
        stat = collections.OrderedDict()
        stat_names = ["load", "taken", "free", "guest",
                     "resident", "admin", "workers", "school"]


        self.diver.select_club("4")
        time.sleep(1)
        date_time = datetime.datetime.now()
        date = date_time.date()
        try:
            for opt in stat_names:
                stat[opt] = self.diver.get_data(opt)
        except Exception as er:
            print(er)
            raise Exception(er)

        seq = [date, date_time, self.clubs["les"].field_name]
        seq.extend(stat.values())
        seq = tuple(seq)

        self.keeper.add_line(sql_keeper.ins_club_stat(), seq)
        self.keeper.commit()

    def web_process_stop(self):
        self.running = False
        self.diver.close()

    @pyqtSlot()
    def web_process_start(self):
        login_id = 'enter_login'
        password_id = 'enter_password'
        submit_name = 'but_m'

        adr = self.parent.gui.form.adress.text()
        login = self.parent.gui.form.login.text()
        password = self.parent.gui.form.password.text()

        try:
            self.diver = webdriver.WebDriver(adr, webdriver.WebDriver.Chrome)
        except selenium.common.exceptions.WebDriverException:
            self.str_web_process.emit("не удалось запустить страницу")
            self.running = False
        else:
            self.str_web_process.emit("запустился драйвер")
            self.diver.log_in(login_id, password_id, submit_name,
                            login, password)
            self.str_web_process.emit("залогинился")

            self.keeper = sql_keeper.Keeper(DATA_FILE)
            self.keeper.open_connect()
            self.keeper.open_cursor()
            self.keeper.create_table(sql_keeper.table())
            self.running = True

        # while self.running:
        #     self.read_data()

        # self.finished.emit()

class Main:
    def __init__(self):
        QtCore.qDebug('something informative')
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(open(CSS_STYLE, "r").read())
        self.init_thread()
        self.gui = ItStat(ICON_DIR)
        self.gui.closeEvent = self.closeEvent
        self.gui.show()
        self.gui.set_tray_icon()
        self.gui.set_menu()

        self.gui.form.start.clicked.connect(self.start)
        self.gui.form.stop.clicked.connect(self.stop)
        self.gui.form.stop.setDisabled(not self.web.running)
        self.gui.form.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gui.statusBar()

        sys.exit(app.exec_())

    def init_thread(self):
        self.web = Web(self)
        self.thread = QThread()
        self.web.str_web_process.connect(self.on_web_process)
        self.web.moveToThread(self.thread)
        self.web.finished.connect(self.thread.quit)
        self.thread.started.connect(self.web.web_process_start)

    def on_web_process(self, line):
        self.gui.form.stop.setDisabled(not self.web.running)
        self.gui.statusBar().showMessage(line)

    def start(self):
        self.thread.start()

    def stop(self):
        self.web.web_process_stop()

    def closeEvent(self, event):
        event.ignore()
        self.gui.hide()
        self.gui.tray_icon.showMessage(
            "Tray Program",
            "Application was minimized to Tray",
            QtWidgets.QSystemTrayIcon.Information, 2000)


if __name__ == '__main__':
    Main()