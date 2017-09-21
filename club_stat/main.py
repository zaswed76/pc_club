import os
import sys

import time, datetime
from PyQt5 import QtWidgets, QtCore

from club_stat import webdriver, config, club
from club_stat.keeper import keeper, json_keeper

from club_stat.gui.itstat import ItStat

adr = "http://adminold.itland.enes.tech/index.php/map"

ROOT = os.path.join(os.path.dirname(__file__))
CSS_STYLE = os.path.join(ROOT, "css/style.css")
DATA_DIR = os.path.join(ROOT, "data")
DATA_FILE = os.path.join(DATA_DIR, "data.JSON")

class Main:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(open(CSS_STYLE, "r").read())
        self.gui = ItStat()
        self.gui.closeEvent = self.closeEvent
        self.gui.show()




        self.keeper = keeper.Keeper(json_keeper.JsonKeeper(DATA_FILE))
        self.keeper.load()
        self.gui.form.start.clicked.connect(self.start)
        self.gui.form.stop.clicked.connect(self.stop)
        sys.exit(app.exec_())



    def write_data(self):
        self.keeper.write()

    def read_data(self):

        d = datetime.datetime.now()
        dt = d.date().strftime('%Y-%m-%d')

        tm = d.time().strftime('%H-%M-%S.%f')
        self.web.select_club("4")
        taken =  self.web.get_data("taken")



        time.sleep(1)

        self.keeper.write()

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
        self.timer.start(1000 * 5)

    def stop(self):
        self.timer.stop()

    def closeEvent(self, *args, **kwargs):
        try:
            self.web.close()
        except AttributeError as er:
            pass
        self.gui.close()


if __name__ == '__main__':
    Main()