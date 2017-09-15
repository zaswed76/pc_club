import sys
from PyQt5 import QtWidgets

from club_stat import webdriver, config, club
from gui.itstat import ItStat

adr = "http://adminold.itland.enes.tech/index.php/map"

login_id = 'enter_login'
password_id = 'enter_password'
submit_name = 'but_m'
login = ""
password = ""
class Main:
    def __init__(self):
        self.web = webdriver.WebDriver(adr, webdriver.WebDriver.Firefox)
        self.web.log_in(login_id, password_id, submit_name,
                        login, password)

def main():
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = ItStat()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()