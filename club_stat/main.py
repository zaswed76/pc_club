import http
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
from club_stat import pth




from club_stat.gui.itstat import ItStat
from club_stat.gui.out_app import OutApp

adr = "http://adminold.itland.enes.tech/index.php/map"

ROOT = os.path.join(os.path.dirname(__file__))
CSS_STYLE = os.path.join(ROOT, "css/style.css")
DATA_DIR = os.path.join(ROOT, "data")
DATA_FILE = os.path.join(DATA_DIR, "data.db")
ICON_DIR = os.path.join(ROOT, "resource/icons")
ETC = os.path.join(ROOT, "etc")
CONFIG_PATH = os.path.join(ETC, "default.json")

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
    str_web_process = pyqtSignal(str, str)

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.running = False
        self.browser_pos_flag = False
        self._change_time = (0, 0, 0)
        self.clubs = club.Clubs()
        self.clubs["les"] = club.Club(club.Club.LES, club.Statistics())


    @property
    def change_time(self):
        return self._change_time

    @change_time.setter
    def change_time(self, qt):
        if isinstance(qt, QtCore.QTime):
            self._change_time = (qt.hour(), qt.minute(), qt.second())

    def read_data(self):
        time.sleep(1)
        stat = collections.OrderedDict()
        stat_names = ["load", "taken", "free", "guest",
                     "resident", "admin", "workers", "school"]

        try:
            time.sleep(1)
        # переключиться на клуб
            self.diver.select_club("4")
        except http.client.CannotSendRequest as er:
            print(er, "main line 80")
        time.sleep(1)
        # получить текущее время
        date_time = datetime.datetime.now()
        date = date_time.date()
        h = date_time.time().hour
        minute = date_time.time().minute
        # получить данные
        try:
            for opt in stat_names:
                stat[opt] = self.diver.get_data(opt)

            stat["visitor"] = sum([int(x) for x in (stat["guest"], stat["resident"], stat["school"])])

        except Exception as er:

            raise Exception(er)

        seq = [date, date_time, h, minute, self.clubs["les"].field_name]
        seq.extend(stat.values())

        seq = tuple(seq)
        self.str_web_process.emit("запись: {} - {} - {}".format(seq[1], seq[2], seq[13]), "none")
        # записать данные
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
            self.str_web_process.emit("запустился драйвер", "none")
            self.diver.log_in(login_id, password_id, submit_name,
                            login, password)
            self.str_web_process.emit("залогинился", "log_in")
            time.sleep(2)

            self.keeper = sql_keeper.Keeper(pth.DATA_FILE_2)
            self.keeper.open_connect()
            self.keeper.open_cursor()
            self.keeper.create_table(sql_keeper.table())
            self.str_web_process.emit("открыта база данных", "none")
            self.running = True

        while self.running:
            try:
                self.read_data()
            except Exception as er:
                print(er)
            if not self.browser_pos_flag:

                self.diver.browser.set_window_position(-10000, 0)
                self.browser_pos_flag = True
            h, m, s = self.change_time
            time.sleep(((h * 3600) + (m*60) + s) - 4)

        self.finished.emit()
        self.browser_pos_flag = False

class Main:

    def __init__(self):
        QtCore.qDebug('something informative')
        self.web_code = dict(log_in=self.save_login)

        self.cfg = config.load(CONFIG_PATH)
        self._init_thread()
        self._init_gui()

    def _init_thread(self):
        self.web = Web(self)
        self.thread = QThread()
        self.web.str_web_process.connect(self.on_web_process)
        self.web.moveToThread(self.thread)
        self.web.finished.connect(self.thread.quit)
        self.thread.started.connect(self.web.web_process_start)

    def _fields_valid(self):
        l = self.gui.form.login.text()
        a = self.gui.form.adress.text()
        p = self.gui.form.password.text()
        r = all([l, a, p])
        return r

    def _init_gui(self):
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(open(CSS_STYLE, "r").read())
        self.gui = ItStat(ICON_DIR)
        self.gui.closeEvent = self.closeEvent
        self.gui.show()
        self.gui.resize(500, 350)
        self.gui.set_tray_icon()
        self.gui.set_menu()

        # start

        self.gui.form.start.clicked.connect(self.start)
        self.gui.form.start.setDisabled(not self._fields_valid())


        self.gui.form.stop.clicked.connect(self.stop)
        self.gui.form.stop.setDisabled(not self.web.running)

        # Export btn

        self.gui.form.export_to_xlsx.clicked.connect(self.export_to_xlsx)



        # Password
        self.gui.form.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gui.form.password.textChanged[str].connect(self._password_changed)
        self.gui.form.password.setPlaceholderText("Пароль")
        # Login
        completer = QtWidgets.QCompleter(self.cfg["logins"])
        self.gui.form.login.setCompleter(completer)
        self.gui.form.login.textChanged[str].connect(self._login_changed)
        self.gui.form.login.setText(self.cfg["last_login"])
        # Address
        completer = QtWidgets.QCompleter(self.cfg["address"])
        self.gui.form.adress.setCompleter(completer)
        self.gui.form.adress.textChanged[str].connect(self._address_changed)
        self.gui.form.adress.setText(self.cfg["last_address"])
        # TimeChange
        self.gui.form.time_edit.setDisplayFormat("HH:mm:ss")
        self.gui.form.time_edit.setMinimumTime(QtCore.QTime(0, 0, 10))
        self.gui.form.time_edit.setTime(QtCore.QTime(*self.cfg["time_change"]))



        self.gui.statusBar()
        sys.exit(app.exec_())


    def _login_changed(self, s):
        self.gui.form.start.setDisabled(not self._fields_valid())

    def _address_changed(self, s):
        self.gui.form.start.setDisabled(not self._fields_valid())

    def _password_changed(self, s):
        self.gui.form.start.setDisabled(not self._fields_valid())

    def on_web_process(self, line, code):
        self.gui.form.stop.setDisabled(not self.web.running)
        self.gui.form.start.setDisabled(self.web.running)
        self.gui.statusBar().showMessage(line)
        self.web_code.get(code, lambda: None)()

    def save_login(self):
        lg = self.gui.form.login.text()
        if lg not in self.cfg["logins"]:
            self.cfg["logins"].append(lg)
        self.cfg["last_login"] = lg
        adr = self.gui.form.adress.text()
        if adr not in self.cfg["address"]:
            self.cfg["address"].append(adr)
        self.cfg["last_address"] = adr
        qt = self.gui.form.time_edit.time()
        self.cfg["time_change"] = [qt.hour(), qt.minute(), qt.second()]
        config.save(CONFIG_PATH, self.cfg)


    def start(self):
        self.web.change_time = self.gui.form.time_edit.time()
        self.thread.start()

    def stop(self):
        self.web.web_process_stop()
        self.gui.form.stop.setDisabled(not self.web.running)
        self.gui.form.start.setDisabled(self.web.running)


    def export_to_xlsx(self):
        out_app = OutApp(pth.DATA_FILE_2)
        out_app.set_step(self.cfg["step_name"])
        out_app.show()

    def closeEvent(self, event):

        event.ignore()
        self.gui.hide()
        self.gui.tray_icon.showMessage(
            "Tray Program",
            "Application was minimized to Tray",
            QtWidgets.QSystemTrayIcon.Information, 2000)


if __name__ == '__main__':
    Main()