import os
import sys
from PyQt5 import QtWidgets, QtCore

from club_stat import webdriver, config, club
from club_stat.keeper import keeper, json_keeper

from club_stat.gui.itstat import ItStat

adr = "http://adminold.itland.enes.tech/index.php/map"

ROOT = os.path.join(os.path.dirname(__file__))
CSS_STYLE = os.path.join(ROOT, "css/style.css")
DATA_DIR = os.path.join(ROOT, "data")

class Main:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(open(CSS_STYLE, "r").read())
        self.gui = ItStat()
        self.gui.show()
        self.keeper = keeper.Keeper(json_keeper.JsonKeeper(DATA_DIR))
        self.gui.form.start.clicked.connect(self.start)
        self.gui.form.stop.clicked.connect(self.stop)
        sys.exit(app.exec_())

    def get_data(self):
        print("получаем данные")
        print("записываем даные")

    def start(self):
        adr = self.gui.form.adress.text()
        login_id = 'enter_login'
        password_id = 'enter_password'
        submit_name = 'but_m'
        login = self.gui.form.login.text()
        password = self.gui.form.password.text()
        # web = webdriver.WebDriver(adr, webdriver.WebDriver.Firefox)
        # web.log_in(login_id, password_id, submit_name,
        #                 login, password)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_data)
        self.timer.start(1000)

    def stop(self):
        self.timer.stop()


if __name__ == '__main__':
    Main()