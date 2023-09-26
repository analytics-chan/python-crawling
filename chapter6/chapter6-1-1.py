# 네이버 이미지 크롤링

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
driver.get('https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%95%84%EC%9D%B4%EC%9C%A0')

# driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
imgs = driver.find_elements(By.XPATH, '//*[@id="main_pack"]/section[2]/div/div[1]/div[1]')

row = 1
for img in imgs:
    src_url = img.find_element(By.XPATH, f'//*[@id="main_pack"]/section[2]/div/div[1]/div[1]/div[{row}]/div/div[1]/a/img')
    row += 1
# img.click()
    print(src_url.get_attribute('src'))

# print(img)