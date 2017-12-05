import os

from club_stat import config, pth
from club_stat.alt_scr.browser import Browser


class Br:
    def __init__(self):
        self.cfg = config.load(pth.CONFIG_PATH)
        self.adr = self.cfg["last_address"]
        self.login_id = 'enter_login'
        self.password_id = 'enter_password'
        self.submit_name = 'but_m'
        self.login = self.cfg["last_login"]
        self._password = "fasadAQ9"

        self.driver_pth = os.path.join(pth.DRIVERS_DIR, self.cfg["driver"])

        self.binary_pth = os.path.abspath(self.cfg["binary_browser_pth"])

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pw):
        self._password = pw

    def get_driver(self):
        self.browser = Browser(self.driver_pth, self.binary_pth)

    def get_page(self):
        self.browser.get_page(self.adr)
        assert "Shell" in self.browser.driver.title

    def log_in(self):
        self.browser.log_in(self.login_id, self.password_id,
                       self.submit_name, self.login, self.password)
        assert "Карта клуба" in self.browser.driver.title


m = Br()
m.get_driver()
m.get_page()
    # m.password = input("введите пароль\n")
    # print(m.password)
m.log_in()

