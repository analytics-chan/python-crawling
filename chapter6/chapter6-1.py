# 네이버 이미지 주소 추출

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%A7%80%EC%88%98"

# main_url = 'https://www.google.com/search?q=%EC%A7%80%EC%88%98&tbm=isch'


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

# driver.get(main_url)

# 무한 스크롤 처리
# 스크롤 전 높이
# before_h = driver.execute_script('return window.scrollY')
before_h = driver.execute_script('return document.body.scrollHeight')

# 무한 스크롤 (반복문)
while True:
#   # 스크롤 사이 페이지 로딩 시간
#   time.sleep(3)

  # 맨 아래로 스크롤 내리기
  # driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)
  
  # 첫번째 스크롤 내리기
  driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

  time.sleep(2)

  # 스크롤 후 높이
#   after_h = driver.execute_script('return window.scrollY')
  after_h = driver.execute_script('return document.body.scrollHeight')


  if after_h == before_h:
    break
  before_h = after_h

imgs = driver.find_elements(By.CSS_SELECTOR, '._image._listImage')
# imgs = driver.find_elements(By.CSS_SELECTOR, '.rg_i.Q4LuWd')

i = 1
for img in imgs:
  empty_src = 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7'
  if img.get_attribute('src') != empty_src:
    img_src = img.get_attribute('src')
    print(i, img_src)
  else:
    try:
      img.click()
      time.sleep(1)
      imgUrl = driver.find_element(By.XPATH, '//*[@id="main_pack"]/section[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[1]/img').get_attribute('src')
      print(i, imgUrl)
    except:
      pass
  i += 1

  # # 각 이미지 태그의 주소
  # img_src = img.get_attribute('src')
  # print(i, img_src)
  # i += 1


