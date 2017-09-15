import sys
from PyQt5 import QtWidgets


from club_stat import webdriver, config, club
from club_stat.gui.itstat import ItStat

adr = "http://adminold.itland.enes.tech/index.php/map"

login_id = 'enter_login'
password_id = 'enter_password'
submit_name = 'but_m'
login = ""
password = ""



def main():

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open('css/style.css', "r").read())
    gui = ItStat()
    gui.show()

    login_id = 'enter_login'
    password_id = 'enter_password'
    submit_name = 'but_m'
    login = ""
    password = ""
    print(gui.form.adress)

    # web = webdriver.WebDriver(adr, webdriver.WebDriver.Firefox)
    # web.log_in(login_id, password_id, submit_name,
    #                     login, password)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()