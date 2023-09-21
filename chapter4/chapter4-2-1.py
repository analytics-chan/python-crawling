# 네이버 뉴스 본문 링크 가져오기(셀레니움 버전 연습)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

# 불필요한 에러 메시지 삭제
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 검색어 설정
keyword = input('검색어를 입력하세요 >>> ')

# 웹페이지 해당 주소 이동
driver.get(f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}')

# 웹페이지 로딩 시 n초 기다림
driver.implicitly_wait(2)

# 화면 최대화
driver.maximize_window()

lists = driver.find_elements(By.CSS_SELECTOR, '.news_wrap.api_ani_send')
# print(lists)

for e, list in enumerate(lists, 1):
    title = list.find_element(By.CSS_SELECTOR, '.news_tit').get_attribute('title')
    link = list.find_element(By.CSS_SELECTOR, '.news_tit').get_attribute('href')
    print(f'{e}) 기사제목: {title} \n 링크: {link}')