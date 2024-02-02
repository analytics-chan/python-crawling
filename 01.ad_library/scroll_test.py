# 메타 광고 라이브러리
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

import time

url = "https://www.naver.com"

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(1)

# driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)

# driver.execute_script('window.scrollTo(0, 500);')

time.sleep(1)