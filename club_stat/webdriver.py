
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
        select.select_by_value(club)


    def get_data(self, field):
        return self.browser.find_element_by_id(field).text

    def close(self):
        self.browser.quit()

    def get_selected_name(self):
        select = Select(self.browser.find_element_by_id('club_id'))
        return [x.text for x in select.options if x]

    def cu(self):
        obj = self.browser.find_element_by_class_name("map_lft")

        rows = obj.find_elements_by_tag_name("tr")  # get all of the rows in the table
        for row in rows:
            col = row.find_elements_by_tag_name("td")[1]
            print(col.text) #prints text from the element



if __name__ == '__main__':
    adr = "http://adminold.itland.enes.tech/index.php/map"
    login_id = 'enter_login'
    password_id = 'enter_password'
    submit_name = 'but_m'
    login = "zaswed"
    password = "fasadAQ9"
    driver = WebDriver(adr, WebDriver.Chrome)
    driver.log_in(login_id, password_id, submit_name,
                            login, password)
    driver.cu()

    driver.close()



