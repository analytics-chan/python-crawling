# 데이터 저장
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

import time
import openpyxl

keyword = input('검색어를 입력하세요 >>> ')

wb = openpyxl.Workbook()
ws = wb.create_sheet(keyword, 0)
ws.append(['순위', '이름', '별점'])

url = 'https://map.naver.com/p'

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)
driver.implicitly_wait(5)
driver.maximize_window()

# 검색창 입력
search = driver.find_element(By.CSS_SELECTOR, 'input.input_search')
search.click()
time.sleep(1)
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(2)

# iframe 안으로 들어가기
driver.switch_to.frame('searchIframe')

# iframe 밖으로 나오기
# driver.switch_to.default_content()

# iframe 내부를 한 번 클릭하기
driver.find_element(By.CSS_SELECTOR, '#_pcmap_list_scroll_container').click()

# 로딩된 데이터 개수 확인
lis = driver.find_elements(By.CSS_SELECTOR, 'li.UEzoS')
before_len = len(lis)

# 무한 스크롤 처리 방법
while True:
    # 맨 아래로 스크롤 내리기
    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1.5)

    # 스크롤 후 로딩된 데이터 개수 확인
    lis = driver.find_elements(By.CSS_SELECTOR, 'li.UEzoS')
    after_len = len(lis)

    # print('스크롤 전 >>> ', before_len, '스크롤 후 >>> ', after_len)

    # 로딩된 데이너 개수가 같다면 반복 멈춤
    if before_len == after_len:
        break
    before_len = after_len

# res = driver.page_source
# soup = BeautifulSoup(res, 'html.parser')

# 데이터 기다리는 시간을 0으로 만들기(데이터가 없더라도 빠르게 넘어감)
driver.implicitly_wait(0)

rank = 1
for li in lis:
    # print(len(li.find_elements(By.CSS_SELECTOR, 'svg.dPXjn')))
    # 광고 상품 아닌 것만
    if len(li.find_elements(By.CSS_SELECTOR, 'svg.dPXjn')) == 0:
        # 별점이 있는 것만 크롤링
        # print(len(driver.find_elements(By.CSS_SELECTOR, 'span.a2RFq')))
        # driver.find_elements(By.CSS_SELECTOR, '별점 CSS 선택자')
        if len(li.find_elements(By.CSS_SELECTOR, 'span.a2RFq')) > 0:
            # 가게명
            name = li.find_element(By.CSS_SELECTOR, 'span.place_bluelink.TYaxT').text
            # 별점
            star = li.find_element(By.CSS_SELECTOR, 'span.h69bs.a2RFq').text.replace('별점\n', '').strip()
            print(rank, name, star)
            ws.append([rank, name, star])
            rank += 1

wb.save(f'chapter11/{keyword}.xlsx')

# 데이터 전처리
# 소수점 있을 경우 float()
# 소수점 없을 경우 int()

# for li in lis:
#     # 목록 프레임으로 이동
#     driver.switch_to.default_content()
#     driver.switch_to.frame('searchIframe')

#     name = li.find_element(By.CSS_SELECTOR,"span.TYaxT")
#     name.click()

#     # 상세 프레임으로 이동
#     browser.switch_to.default_content()
#     browser.switch_to.frame('entryIframe')

#     # 블로그 리뷰수 가져오기
#     visit_review = browser.find_element(By.CSS_SELECTOR, "#app-root > div > div > div > div.place_section.OP4V8 > div.zD5Nm.f7aZ0 > div.dAsGb > span:nth-child(2) > a")
#     print(visit_review.text)
#     time.sleep(1)