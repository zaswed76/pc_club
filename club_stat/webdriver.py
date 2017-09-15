
from selenium import webdriver
from selenium.webdriver.support.ui import Select

enter_login = 'enter_login'
enter_password = 'enter_password'
submit = 'but_m'

class WebDriver:
    Firefox = webdriver.Firefox
    def __init__(self, adr, browser):
        self.browser = browser()
        self.browser.get(adr)

    def log_in(self, login_id, password_id, submit_name,
                        login, password):
        username = self.browser.find_element_by_id(login_id)
        username.send_keys(login)
        passw = self.browser.find_element_by_id(password_id)
        passw.send_keys(password)
        m = self.browser.find_element_by_class_name(submit_name)
        m.click()