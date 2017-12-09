import os

from club_stat import pth
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import selenium.webdriver.chrome.service as service

from bs4 import BeautifulSoup



enter_login = 'enter_login'
enter_password = 'enter_password'
submit = 'but_m'

class WebDriver:
    Firefox = webdriver.Firefox
    Chrome = webdriver.Chrome
    def __init__(self, adr, driver_pth, binary_pth):
        self.binary_pth = binary_pth
        self.driver_pth = driver_pth

        self.service = service.Service(self.driver_pth)
        self.service.start()
        self.browser = self._driver()
        self.browser.get(adr)
        self.browser.maximize_window()

    def refresh(self):
        self.browser.refresh()


    def _driver(self) -> webdriver.Remote:
        capabilities = {'chrome.binary': self.binary_pth}
        driver = webdriver.Remote(self.service.service_url, capabilities)
        return driver

    def log_in(self, login_id, password_id, submit_name,
                        login, password):
        username = self.browser.find_element_by_id(login_id)
        username.send_keys(login)
        passw = self.browser.find_element_by_id(password_id)
        passw.send_keys(password)
        m = self.browser.find_element_by_class_name(submit_name)
        m.click()

    def select_club(self, club:str):
        select = Select(self.browser.find_element_by_id('club_id'))
        select.select_by_value(club)


    def get_data(self, field):
        return self.browser.find_element_by_id(field).text

    def close(self):
        self.browser.quit()

    def get_selected_name(self):
        select = Select(self.browser.find_element_by_id('club_id'))
        return [x.text for x in select.options if x]

    def get_table(self):
        text = self.browser.page_source
        soup = BeautifulSoup(text)
        soup.findAll('b')





if __name__ == '__main__':
    from club_stat import pth, config
    cfg = config.load(pth.CONFIG_PATH)
    adr = "http://adminold.itland.enes.tech/index.php/map"
    login_id = 'enter_login'
    password_id = 'enter_password'
    submit_name = 'but_m'
    login = "zaswed"
    password = "fasadAQ9"
    driver_pth = os.path.join(pth.DRIVERS_DIR,
                                  cfg["driver"])
    binary_pth = os.path.abspath(cfg["binary_browser_pth"])
    driver = WebDriver(adr, driver_pth, binary_pth)
    driver.log_in(login_id, password_id, submit_name,
                            login, password)
    driver.get_table()
    driver.close()




