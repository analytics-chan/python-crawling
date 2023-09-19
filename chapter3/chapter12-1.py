# 네이버 쇼핑 크롤링 무한 스크롤 => csv 파일로 저장하기
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
driver.get('https://www.naver.com')
driver.implicitly_wait(10) # 로딩이 끝날 때까지 10초 기다림

# 쇼핑 메뉴 클릭
driver.find_element(By.CSS_SELECTOR, '#shortcutArea > ul > li:nth-child(4) > a').click()
time.sleep(2)

# 새 창에서 작업 진행해야 함
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

# 화면 최대화
driver.maximize_window()

# 검색창 클릭
search = driver.find_element(By.CSS_SELECTOR, 'input._searchInput_search_text_3CUDs')
# search = driver.find_element(By.CLASS_NAME, '_searchInput_search_text_3CUDs')
# search = driver.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div[1]/input')
search.click()

# 검색어 입력
search.send_keys('아이폰 14')
search.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = driver.execute_script('return window.scrollY')

# 무한 스크롤 (반복문)
while True:
  # 맨 아래로 스크롤 내리기
  driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)

  # 스크롤 사이 페이지 로딩 시간
  time.sleep(2)

  # 스크롤 후 높이
  after_h = driver.execute_script('return window.scorllY')

  if after_h == before_h:
    break
  before_h = after_h

# 파일 생성
f = open(r"C:\Users\withbrother\Desktop\python_test2\chapter3\네이버쇼핑몰크롤링TEST.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)

# 상품 정보 div
items = driver.find_elements(By.CSS_SELECTOR, '.product_item__MDtDF')

for item in items:
  # name = item.find_element(By.CSS_SELECTOR, '.product_link__TrAac.linkAnchor').text
  name = item.find_element(By.CSS_SELECTOR, 'div.product_title__Mmw2K > a').get_attribute('title')
  price = item.find_element(By.CSS_SELECTOR, 'span.price_num__S2p_v > em').text
  link = item.find_element(By.CSS_SELECTOR, 'div.product_title__Mmw2K > a').get_attribute('href')
  print(name, price, link)
  # 데이터 저장
  csvWriter.writerow([name, price, link])

# 파일 닫기
f.close()
