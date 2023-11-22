# 올리브영
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time
import datetime

today = datetime.datetime.today()
year = str(today.year)
month = str(today.month)
day = str(today.day)

url = "https://www.oliveyoung.co.kr/"

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)

query_box = driver.find_element(By.CSS_SELECTOR, 'div.placeholder_area')
query_box.click()

query_input = driver.find_element(By.CSS_SELECTOR, '#query')
query_input.send_keys('수분크림')