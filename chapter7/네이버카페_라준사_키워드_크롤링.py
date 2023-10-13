# 네이버 카페 '라준사' 키워드 크롤링

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import openpyxl

import time

wb = openpyxl.Workbook()

ws = wb.create_sheet('누네안과_키워드', 0)

ws.column_dimensions['A'].width = 70
ws.column_dimensions['C'].width = 25
ws.column_dimensions['D'].width = 10

ws.append(['제목', '댓글수', '작성자', '작성일', '조회수', '키워드'])

url = "https://cafe.naver.com/navercafezz"

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)

# 검색창 클릭
search = driver.find_element(By.CSS_SELECTOR, '#topLayerQueryInput')
search.click()
search.send_keys('누네안과')
# search.send_keys('ㄴㄴ안과')
# search.send_keys('강남누네')

driver.find_element(By.CSS_SELECTOR, '#cafe-search > form > .btn').click()

time.sleep(2)

driver.switch_to.frame('cafe_main')

driver.find_element(By.CSS_SELECTOR, '#listSizeSelectDiv > a').click()
driver.find_element(By.CSS_SELECTOR, '#listSizeSelectDiv > ul > li:nth-child(7) > a').click()

page_len = len(driver.find_elements(By.CSS_SELECTOR, '.prev-next > a'))

print(page_len)

if page_len == 0:
    print('등록된 게시물이 없습니다.')
else:
    for i in range(2, 20):
        res = driver.page_source
        soup = BeautifulSoup(res, 'html.parser')

        trs = soup.select('#main-area > div:nth-child(5) > table > tbody > tr')

        print(i - 1, '페이지-------------------')

        for tr in trs:
            try:
                title = tr.select_one('a.article').text.strip().replace('\n', '').replace('         ', '')
                writer = tr.select_one('.p-nick > .m-tcol-c').text
                date = tr.select_one('.td_date').text
                view_count = tr.select_one('.td_view').text
            except:
                pass
        
            try:
                review_count = tr.select_one('a.cmt > em').text.strip()
            except:
                review_count = 0

            print(title, review_count, writer, date, view_count)

            ws.append([title, int(review_count), writer, date, view_count, '키워드'])

            # time.sleep(1)
        try:
            if i%10 == 1:
                driver.find_element(By.CLASS_NAME, 'pgR').click()
            else:
                driver.find_element(By.LINK_TEXT, str(i)).click()
        except Exception as e:
            print('----END---')
            break


    # time.sleep(1)

wb.save('chapter7/20231013 누네안과_키워드.xlsx')