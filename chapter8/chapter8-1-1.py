# 구글 이미지 크롤링 연습
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
import requests
from urllib import request
from urllib.request import Request, urlopen
import urllib.request
from webdriver_manager.chrome import ChromeDriverManager

keyword = input('검색어를 입력해주세요 >>> ')

if not os.path.exists(f'chapter8/{keyword}'):
    os.mkdir(f'chapter8/{keyword}')

url = f"https://www.google.com/search?q={keyword}&tbm=isch"

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)

before_h = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    time.sleep(2)

    after_h = driver.execute_script('return document.body.scrollHeight')

    if after_h == before_h:
        break
    before_h = after_h

imgs = driver.find_elements(By.CSS_SELECTOR, '.rg_i.Q4LuWd')

for i, img in enumerate(imgs, 1):
    img.click()
    time.sleep(1)
    imgUrl = driver.find_element(By.CSS_SELECTOR, '.r48jcc.pT0Scc').get_attribute('src')
    print(i, imgUrl)
    urllib.request.urlretrieve(imgUrl, f'chapter8/{keyword}/{i}.jpg')
    if i == 50:
        break

    # try:
    #     img.click()
    #     time.sleep(1)
    #     imgUrl = driver.find_element(By.CSS_SELECTOR, '.r48jcc.pT0Scc.iPVvYb').get_attribute('src')
    #     print(i, imgUrl)
    # except:
    #     img.click()
    #     time.sleep(1)
    #     imgUrl = driver.find_element(By.CSS_SELECTOR, '.r48jcc.pT0Scc').get_attribute('src')
    #     print(i, imgUrl)
    