import os
import sys
from PyQt5 import QtWidgets, uic
from club_stat import webdriver, config, club

ui_pth = r"C:\Users\Cassa\Desktop\Serg\project\pc_club\club_stat\gui\ui\itstat.ui"


class ItStat(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.center = QtWidgets.QFrame()
        self.setCentralWidget(self.center)
        self.form = uic.loadUi(ui_pth, self.center)

        self.form.start.clicked.connect(
            self.start)



    def start(self):
        adr = self.form.adress.text()
        login_id = 'enter_login'
        password_id = 'enter_password'
        submit_name = 'but_m'
        login = self.form.login.text()
        password = self.form.password.text()
        web = webdriver.WebDriver(adr, webdriver.WebDriver.Firefox)
        web.log_in(login_id, password_id, submit_name,
                        login, password)



if __name__ == '__main__':
    UI_DIR = "../club_stat/gui/ui"
    ui_pth = r"C:\Users\Cassa\Desktop\Serg\project\pc_club\club_stat\gui\ui\itstat.ui"
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = ItStat()
    main.show()
    sys.exit(app.exec_())