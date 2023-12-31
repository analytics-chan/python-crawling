# 검색어 입력
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time

url = 'https://map.naver.com/p'

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)
driver.implicitly_wait(5)
driver.maximize_window()

# 검색창 입력
search = driver.find_element(By.CSS_SELECTOR, 'input.input_search')
search.click()
time.sleep(1)
search.send_keys('강남역 맛집')
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(2)
