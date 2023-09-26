# 폴더 생성 후 이미지 다운로드하기
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request

# 검색어 입력
keyword = input('검색어를 입력하세요 >>> ')

# 폴더가 있을 경우 생성하지 않음
if not os.path.exists(f'chapter6/{keyword}'):
    os.mkdir(f'chapter6/{keyword}')

url = f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={keyword}"

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)

# 무한 스크롤 처리
# 스크롤 전 높이
before_h = driver.execute_script('return document.body.scrollHeight')

while True:  
  # 첫번째 스크롤 내리기
  driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

  time.sleep(2)

  # 스크롤 후 높이
  after_h = driver.execute_script('return document.body.scrollHeight')

  if after_h == before_h:
    break
  before_h = after_h

imgs = driver.find_elements(By.CSS_SELECTOR, '._image._listImage')

for i, img in enumerate(imgs, 1):
  empty_src = 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7'
  if img.get_attribute('src') != empty_src:
    img_src = img.get_attribute('src')
    # print(i, img_src)
    urllib.request.urlretrieve(img_src, f'chapter6/{keyword}/{i}.png')
  else:
    try:
      img.click()
      time.sleep(1)
      imgUrl = driver.find_element(By.XPATH, '//*[@id="main_pack"]/section[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[1]/img').get_attribute('src')
      # print(i, imgUrl)
      urllib.request.urlretrieve(imgUrl, f'chapter6/{keyword}/{i}.png')
    except:
      pass


# urllib.request.urlretrieve(저장할 이미지 url, 저장할 경로)