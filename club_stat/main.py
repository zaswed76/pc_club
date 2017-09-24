import os
import sys

import collections
import time, datetime
from PyQt5 import QtWidgets, QtCore

from club_stat import webdriver, config, club
from club_stat.sql import sql_keeper

from club_stat.gui.itstat import ItStat

adr = "http://adminold.itland.enes.tech/index.php/map"

ROOT = os.path.join(os.path.dirname(__file__))
CSS_STYLE = os.path.join(ROOT, "css/style.css")
DATA_DIR = os.path.join(ROOT, "data")
DATA_FILE = os.path.join(DATA_DIR, "data.db")

class Main:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(open(CSS_STYLE, "r").read())
        self.gui = ItStat()
        self.gui.closeEvent = self.closeEvent
        self.gui.show()



        self.clubs = club.Clubs()
        self.clubs["les"] = club.Club(club.Club.LES, club.Statistics())

        self.gui.form.start.clicked.connect(self.start)
        self.gui.form.stop.clicked.connect(self.stop)
        sys.exit(app.exec_())



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
        self.web.log_in(login_id, password_id, submit_name,
                        login, password)

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

    def closeEvent(self, *args, **kwargs):
        try:
            self.web.close()
            self.keeper.close()
        except AttributeError as er:
            print(er)
        self.gui.close()


if __name__ == '__main__':
    Main()