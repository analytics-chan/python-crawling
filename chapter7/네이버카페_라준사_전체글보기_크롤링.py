# 네이버 카페 '라준사' 전체글보기 998페이지 크롤링

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import openpyxl

import time

wb = openpyxl.Workbook()

ws = wb.create_sheet('전체글보기', 0)

ws.column_dimensions['A'].width = 20
ws.column_dimensions['B'].width = 70
ws.column_dimensions['D'].width = 25
ws.column_dimensions['E'].width = 10

ws.append(['카테고리', '제목', '댓글수', '작성자', '작성일', '조회수'])

url = "https://cafe.naver.com/navercafezz"

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)

# 전체글보기 클릭
driver.find_element(By.CSS_SELECTOR, '#menuLink0').click()

time.sleep(2)

driver.switch_to.frame('cafe_main')

# 50개씩 보기
driver.find_element(By.CSS_SELECTOR, '#listSizeSelectDiv > a').click()
driver.find_element(By.CSS_SELECTOR, '#listSizeSelectDiv > ul > li:nth-child(7) > a').click()

#listSizeSelectDiv > ul > li:nth-child(7) > a

# driver.find_element(By.LINK_TEXT)

# 18페이지까지 가져옴
# for i in range(2, 20):
#     article = driver.find_elements(By.CLASS_NAME, 'article-board')
#     trs = article[1].find_elements(By.CSS_SELECTOR, '#main-area > div:nth-child(4) > table > tbody > tr')

#     print(i, '페이지-----------------')

#     for tr in trs:
#         try: 
#             cate = tr.find_element(By.CSS_SELECTOR, '.inner_name > a.link_name').text
#             title = tr.find_element(By.CSS_SELECTOR, 'a.article').text
#         except:
#             pass

#         try:
#             review_count = tr.find_element(By.CSS_SELECTOR, 'a.cmt > em').text
#         except:
#             review_count = 0

#         if cate != '가입인사':
#             print(cate, title, review_count)


#     if i%10 == 1:
#         driver.find_element(By.CLASS_NAME, 'pgR').click()
#     else:
#         driver.find_element(By.LINK_TEXT, str(i)).click()

#     time.sleep(1)

# 1 ~ 998페이지까지 크롤링
for i in range(2, 1000):
    res = driver.page_source
    soup = BeautifulSoup(res, 'html.parser')

    article = soup.select('.article-board')
    trs = article[1].select('#main-area > div:nth-child(4) > table > tbody > tr')

    print(i - 1, '페이지-------------------')

    for tr in trs:
        try:
            cate = tr.select_one('a.link_name').text.strip()
            title = tr.select_one('a.article').text.strip()
            writer = tr.select_one('.p-nick > .m-tcol-c').text
            date = tr.select_one('.td_date').text
            view_count = tr.select_one('.td_view').text
        except:
            pass

        try:
            review_count = tr.select_one('a.cmt > em').text.strip()
        except:
            review_count = 0

        # 가입인사 카테고리 제외
        if cate != '가입인사':
            # print(cate, title.replace('\n', '').replace('         ', ''), review_count, writer, date, view_count)
            ws.append([cate, title.replace('\n', '').replace('         ', ''), int(review_count), writer, date, view_count])

        # time.sleep(1)

    if i%10 == 1:
        driver.find_element(By.CLASS_NAME, 'pgR').click()
    else:
        driver.find_element(By.LINK_TEXT, str(i)).click()

    time.sleep(1)

wb.save('chapter7/20231013 전체글보기2.xlsx')