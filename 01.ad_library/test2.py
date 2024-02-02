from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import urllib.request as req
import time
import datetime

#1_날짜 설정
now = datetime.datetime.now()
nowDate = now.strftime('%Y-%m-%d')

#2-1_URL 접근
# url = input("URL : ")

keyword = input('검색어를 입력해주세요 >>> ')

url = f"https://ko-kr.facebook.com/ads/library/?active_status=all&ad_type=all&country=KR&q={keyword}&search_type=keyword_unordered&media_type=all"

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)

#2-2_스크롤 다운
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#2-3_이미지 취합 및 타이틀 획득
html = driver.page_source
soup = bs(html, 'html.parser')
images = soup.find_all(class_= '_7jys img')
title = soup.find(class_= 'qku1pbnj d0wue5ts cu1gti5y pw7auppr te7ihjl9 svz86pwt a53abz89 dnk81rqm gp6ucdfj').string

#2-4_이미지 저장
i = 1
for image in images :
    imageUrl = image['src']
    req.urlretrieve(imageUrl, './Image/' + title +"_" + str(i) + "_" + str(nowDate) + '.jpg')
    i += 1

#3_종료
driver.quit()
print("Complte")