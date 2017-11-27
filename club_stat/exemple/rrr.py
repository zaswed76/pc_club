


import os

from club_stat import pth




import time

from selenium import webdriver
import selenium.webdriver.chrome.service as service
dr = os.path.join(pth.ROOT, "chromedriver.exe")
service = service.Service(dr)
service.start()
capabilities = {'chrome.binary': "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"}
driver = webdriver.Remote(service.service_url, capabilities)
driver.get('http://www.google.com/xhtml')
time.sleep(5) # Let the user actually see something!
driver.quit()