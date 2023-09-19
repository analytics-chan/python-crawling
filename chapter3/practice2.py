# 네이버 로그인 자동화

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
driver.implicitly_wait(5) # 웹페이지가 로딩 될 때까지 5초 기다림
driver.maximize_window() # 화면 최대화
driver.get('https://play.google.com/store/apps/details?id=com.starbucks.co&hl=ko-KR')

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# reviews = driver.find_element(By.CSS_SELECTOR, '#ow72 > section > div > div.Jwxk6d > div:nth-child(5) > div > div > button')
# reviews = driver.find_element(By.CLASS_NAME, 'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-dgl2Hf ksBjEc lKxP2d LQeN7 aLey0c')
allreview = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/c-wiz[4]/section/div/div[2]/div[5]/div/div/button/span')
time.sleep(1)

allreview.click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# 파일 생성
# f = open(r"C:\Users\withbrother\Desktop\python_test2\chapter3\스타벅스리뷰TEST.csv", 'w', encoding='UTF-8', newline='')
f = open(r"C:\Users\withbrother\Desktop\python_test2\chapter3\스타벅스리뷰TEST2.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)

# 리뷰 전체 div
# review = driver.find_elements(By.XPATH, '//*[@id="yDmH0d"]/div[4]/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]')
# r = driver.find_elements(By.CLASS_NAME, 'h3YV2d')
reviews = driver.find_elements(By.CLASS_NAME, 'RHo1pe')

# print(t)

for review in reviews:
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  date = review.find_element(By.CSS_SELECTOR, 'span.bp9Aid').text
  star = review.find_element(By.CSS_SELECTOR, 'div.iXRFPc').get_attribute('aria-label')
  comment = review.find_element(By.CSS_SELECTOR, 'div.h3YV2d').text
  print(date, star, comment)
  csvWriter.writerow([date, star, comment])

f.close()


# row = 1
# for t in r:
#   test = t.text
#   print(f'[{row}] => {test}')
#   row = row + 1