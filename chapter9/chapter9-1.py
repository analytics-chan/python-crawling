# 키워드별 크롤링
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

keyword = input('검색어를 입력하세요 >>> ')
url = f'https://www.youtube.com/results?search_query={keyword}'

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-loggin'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(10)
driver.maximize_window()
driver.get(url)

# 7번 스크롤
scroll_count = 7

i = 1
while True:
    # 맨 아래로 스크롤 내리기
    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)

    # 스크롤 사이에 페이지 로딩 시간
    time.sleep(2)

    if i == scroll_count:
        break
    i += 1

# Selenium - Beautifulsoup 연동
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

cards = soup.select('div.text-wrapper')

for card in cards:
    # 원하는 정보 가져오기

    #제목
    title = card.select_one('a#video-title').text

    try:
        # 조회수
        view = card.select_one('#metadata-line > span:nth-child(3)').text

        # 날짜
        date = card.select_one('#metadata-line > span:nth-child(4)').text
    except:
        view = "조회수 0회"
        date = "날짜 없음"

    print(title, view, date)