# 틱톡 쇼츠
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

import time
import datetime

today = datetime.datetime.today()
year = str(today.year)
month = str(today.month)
day = str(today.day)

url = "https://www.tiktok.com/foryou"

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)

gue = driver.find_element(By.CSS_SELECTOR, '#loginContainer > div > div > div.css-txolmk-DivGuestModeContainer.exd0a435 > div > div > div > div > div')

time.sleep(1)

gue.click()

shorts = driver.find_elements(By.CSS_SELECTOR, '#main-content-homepage_hot > div.css-9fq6q2-DivOneColumnContainer.e108hwin0 > div')
print(len(shorts))

#loginContainer > div > div > div.css-txolmk-DivGuestModeContainer.exd0a435 > div > div > div > div > div
#loginContainer > div > div > div.css-txolmk-DivGuestModeContainer.exd0a435 > div > div.css-u3m0da-DivBoxContainer.e1cgu1qo0 > div > div > div