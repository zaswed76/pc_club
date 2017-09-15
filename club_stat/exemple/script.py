

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


browser = webdriver.Firefox()


browser.get("http://adminold.itland.enes.tech/index.php/map")

username = browser.find_element_by_id('enter_login')
username.send_keys("")
passw = browser.find_element_by_id('enter_password')
passw.send_keys("")

m = browser.find_element_by_class_name('but_m')
print(m)
m.click()

select = Select(browser.find_element_by_id('club_id'))

# select.select_by_visible_text('IT Land Les')
select.select_by_value('4')


taken = browser.find_element_by_id('taken')
print(taken.text)

def get_taken():
    clubs_names = ["IT Land DreamTown",
                   "IT Land Les",
                   "IT Land Akadem",
                   "IT Land Troya"]

# elem = driver.find_element_by_name("q")
# elem.send_keys("news")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()


