from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
driver.implicitly_wait(5)
driver.maximize_window()
# driver.get('https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%95%84%EC%9D%B4%EC%9C%A0')

driver.get('https://www.google.com/search?q=%EC%A7%80%EC%88%98&tbm=isch')

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

# def infinite_scroll_down(driver, wait=.5):
#     body = driver.find_element(By.TAG_NAME, 'body')
#     while True:
#         body.send_keys(Keys.END)
#         if driver.find_elements(By.XPATH, '//div[contains(@class,"photo_loading")]')[0].get_attribute('style') == '':
#             time.sleep(wait)
#         else:
#             break

# def get_thumbnail_urls(driver, wait=.1, retry=3):
#   empty_src = 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7'
#   urls = []
#   imgs = driver.find_elements(By.XPATH, '//img[@class="_image _listImage"]')
#   for img in imgs:
#     count = retry
#     while count:
#       src = img.get_attribute('src')
#       if src == empty_src:
#         src = img.get_attribute('data-lazy-src')
#       if src is not None and src != empty_src:
#         urls += [src]
#         break
#       count -= 1
#       time.sleep(wait)
#   print(f'{len(urls)/len(imgs)} images are loaded')
#   return urls


def get_image_urls(driver, wait=.1, retry=3):
  def check_loaded(img):
    return False if img.get_attribute('src').endswith('type=a340') else True
  
  body = driver.find_element(By.TAG_NAME, 'body')
  body.send_keys(Keys.HOME)
  imgs = driver.find_elements(By.XPATH, '//img[@class="_image _listImage"]')
  urls = []
  for n, img in enumerate(imgs):
    if n == 0:
      img.click()
    count = retry
    origin_img = driver.find_element(By.XPATH, '//div[@class="image _imageBox"]//img')
    while count and not check_loaded(origin_img):
      time.sleep(wait)
      count -= 1

    if check_loaded(origin_img):
      urls.append(origin_img.get_attribute('src'))
    
    body.send_keys(Keys.RIGHT)
  print(f'{len(urls)}/{len(imgs)} images are loaded')
  return urls