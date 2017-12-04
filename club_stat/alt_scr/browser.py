

import http
import os
import sys

import collections
import datetime
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time
import selenium
import club_stat
from club_stat import webdriver, config, club
from club_stat.sql import sql_keeper
from club_stat import pth

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import selenium.webdriver.chrome.service as service

class Browser:
    def __init__(self, driver_pth, binary_pth):
        self.binary_pth = binary_pth
        self.driver_pth = driver_pth

        self.service = service.Service(self.driver_pth)
        self.service.start()
        self.driver = self.get_driver()
        print(self.driver)

        # self.driver.maximize_window()

    def get_driver(self):
        capabilities = {'chrome.binary': self.binary_pth}
        driver = webdriver.Remote(self.service.service_url, capabilities)
        return driver

    def get_page(self, adr):
        self.driver.get(adr)


    def log_in(self):

        """
        залогинится
        """
        return


if __name__ == '__main__':
    adr = "http://adminold.itland.enes.tech/index.php/map"
    login_id = 'enter_login'
    password_id = 'enter_password'
    submit_name = 'but_m'
    login = "zaswed"
    password = "fasadAQ9"


    cfg = config.load(pth.CONFIG_PATH)
    driver_pth = os.path.join(pth.DRIVERS_DIR,
                                  cfg["driver"])
    binary_pth = os.path.abspath(cfg["binary_browser_pth"])

    browser = Browser(driver_pth, binary_pth)
