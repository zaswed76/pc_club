
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import http

enter_login = 'enter_login'
enter_password = 'enter_password'
submit = 'but_m'

class WebDriver:
    Firefox = webdriver.Firefox
    Chrome = webdriver.Chrome
    def __init__(self, adr, browser):
        self.browser = browser()
        self.browser.get(adr)
        self.browser.maximize_window()


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
        if club.isdigit():

            select.select_by_value(club)
        else:
            select.select_by_visible_text(club)

    def get_data(self, field):
        return self.browser.find_element_by_id(field).text

    def close(self):
        self.browser.quit()

if __name__ == '__main__':
    dr = WebDriver("http://adminold.itland.enes.tech/index.php/main", WebDriver.Firefox)