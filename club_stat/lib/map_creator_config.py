import os, re
from club_stat.webdriver import WebDriver
from bs4 import BeautifulSoup

class MapCreator(WebDriver):
    def __init__(self, adr, driver_pth, binary_pth):
        super().__init__(adr, driver_pth, binary_pth, )

    def get_table(self):
        text = self.browser.page_source
        soup = BeautifulSoup(text)
        table = soup.find('table', id="map")
        for tr in table.find_all('tr'):
            for d in tr:
                t = d.findAll("span")
                if t:
                    tag = t[0]
                    print(tag)
                    print(re.sub(r'span', '', str(tag)))

                    print("----------------------")
                """<span class="comp bg_off" data-id="111237" data-ip="172.16.11.48" data-mac="00:24:21:a0:d9:54" data-unauth="" id="pc111237" title="">48</span>"""
            # for i in tr:
            #     for span_tag in i.findAll('span'):
            #         span_tag.replace_with('')
            #         print(i)
                    # print(span[0].extract())
                    # print(span[0].replace_with(""))
                    # new_tag = soup.new_tag("")
                    # new_tag.string = "example.net"
                    # span[0].i.replace_with(new_tag)
                    # print(span[0].find(True))
                    # r = [x.extract() for x in i.findAll("span")]
                    # print("------------------")
                # except AttributeError:
                #     pass
                # print("-----------------")
                # # r = i.findAll("span", id="pc111253")
                # # if r:
                # #     print(r)
                # #     print("------------------------")

from club_stat import pth, config
import time
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
driver = MapCreator(adr, driver_pth, binary_pth)
driver.log_in(login_id, password_id, submit_name,
                        login, password)
time.sleep(1)

driver.select_club("4")
time.sleep(1)
driver.get_table()
driver.close()
