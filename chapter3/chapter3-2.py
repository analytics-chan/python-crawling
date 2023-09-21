# 네이버 쇼핑 크롤링
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