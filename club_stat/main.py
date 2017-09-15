import sys
from PyQt5 import QtWidgets

from club_stat import webdriver, config, club

from club_stat.gui.itstat import ItStat

adr = "http://adminold.itland.enes.tech/index.php/map"

class Main:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        app.setStyleSheet(open('css/style.css', "r").read())
        self.gui = ItStat()
        self.gui.show()
        self.gui.form.start.clicked.connect(
            self.start)

        sys.exit(app.exec_())

    def start(self):
        adr = self.gui.form.adress.text()
        login_id = 'enter_login'
        password_id = 'enter_password'
        submit_name = 'but_m'
        login = self.gui.form.login.text()
        password = self.gui.form.password.text()
        web = webdriver.WebDriver(adr, webdriver.WebDriver.Firefox)
        web.log_in(login_id, password_id, submit_name,
                        login, password)

def main():
    main = Main()



if __name__ == '__main__':
    Main()