

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
from club_stat.alt_scr import passw
import time

class Browser:
    def __init__(self, driver_pth, binary_pth):
        self.binary_pth = binary_pth
        self.driver_pth = driver_pth

        self.service = service.Service(self.driver_pth)
        self.service.start()
        self.driver = self.get_driver()




        # self.driver.maximize_window()

    def get_driver(self):
        capabilities = {'chrome.binary': self.binary_pth}
        driver = webdriver.Remote(self.service.service_url, capabilities)
        return driver

    def get_page(self, adr):
        self.driver.get(adr)


    def log_in(self, login_id, password_id, submit_name,
                        login, password):
        username = self.driver.find_element_by_id(login_id)
        username.send_keys(login)
        passw = self.driver.find_element_by_id(password_id)
        passw.send_keys(password)
        m = self.driver.find_element_by_class_name(submit_name)
        m.click()

    def select_club(self, club:str):
        select = Select(self.driver.find_element_by_id('club_id'))
        select.select_by_value(club)

    def get_data(self, field):
        return self.driver.find_element_by_id(field).text

if __name__ == '__main__':
    adr = "http://adminold.itland.enes.tech/index.php/map"
    login_id = 'enter_login'
    password_id = 'enter_password'
    submit_name = 'but_m'
    login = "zaswed"
    password = "fasadAQ9"


    cfg = config.load(pth.CONFIG_PATH)
    driver_pth = os.path.join(pth.DRIVERS_DIR, cfg["driver"])

    binary_pth = os.path.abspath(cfg["binary_browser_pth"])

    browser = Browser(driver_pth, binary_pth)
    browser.get_page(adr)
    assert "Shell" in browser.driver.title
    while True:
        login = passw.get_log()
        password = passw.get_pass()
        browser.log_in(login_id, password_id, submit_name, login, password)
        if "Карта клуба" in browser.driver.title:
            print("вошли в карту клуба")
            break


    for i in range(1, 5):
        browser.select_club(str(i))
        print(browser.get_data("taken"))
        time.sleep(1)
