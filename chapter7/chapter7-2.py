import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import pyautogui
import openpyxl

wb = openpyxl.Workbook()

ws = wb.create_sheet('미니쉬', 0)

# 열 너비 조정
ws.column_dimensions['B'].width = 60
ws.column_dimensions['C'].width = 20
ws.column_dimensions['D'].width = 12

ws.append(['코드', '제목', '작성자', '날짜', '조회수'])

url = "https://cafe.naver.com/feko"

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)

login = driver.find_element(By.CSS_SELECTOR, 'span.gnb_txt')
login.click()

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, '#id')
id.click()
pyperclip.copy('t3smsi')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, '#pw')
pw.click()
pyperclip.copy('qmfkej1!')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 로그인 버튼 클릭
btn = driver.find_element(By.CSS_SELECTOR, '#log\.login')
btn.click()

clubId = 10912875
menuId = ''
pageNum = 1
userDisplay = 50
keyword = input('검색어를 입력해주세요 >>> ')

# 검색창 클릭
search = driver.find_element(By.CSS_SELECTOR, '#topLayerQueryInput')
search.click()
# search.send_keys('미니쉬')
search.send_keys(keyword)

btn = driver.find_element(By.CSS_SELECTOR, '#cafe-search > form > button')
btn.click()

driver.switch_to.frame("cafe_main")

selectBox = driver.find_element(By.CSS_SELECTOR, '#listSizeSelectDiv > a')
selectBox.click()

select50 = driver.find_element(By.CSS_SELECTOR, '#listSizeSelectDiv > ul > li:nth-child(7) > a')
select50.click()

s = driver.find_element(By.CSS_SELECTOR, 'a#currentSearchByTop')
s.click()

st = driver.find_element(By.CSS_SELECTOR, '#sl_general > li:nth-child(2) > a')
st.click()

b = driver.find_element(By.CSS_SELECTOR, '#main-area > div.search_result > div:nth-child(1) > form > div.input_search_area > button')
b.click()

res = driver.page_source
soup = BeautifulSoup(res, 'html.parser')

lists = soup.select('#main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr')
#main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child(1)
#main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child(2)

# print(lists)

for l in lists:
    id = l.select_one('div.inner_number').text
    # for t in id:
    #     print(t.text)
    title = l.select_one('a.article').text.strip()
    # print(id, title)

print(len(driver.find_elements(By.CSS_SELECTOR, '.prev-next > a')))
# 10 이상일 경우 다음 버튼 눌러야 함

# if i < 9:
#         # i += 1
#         # print('i += 1???', i)
#         driver.find_element(By.XPATH, f'//*[@id="main-area"]/div[7]/a[{i}+1]').click()
#         # print('driver[i]???', i)
#         if i == 10:
#             break
#main-area > div.prev-next > a:nth-child(3)

# //*[@id="main-area"]/div[7]/a[1]
# //*[@id="main-area"]/div[7]/a[2]

#main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child(1)
#main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child(2)

# driver.get(url + '/ArticleSearchList.nhn?search.clubid=' + str(clubId) + '&search.menuid=' + str(menuId) + '&search.page=' + str(pageNum) + '&userDisplay=' + str(userDisplay) + '&search.query=%B9%CC%B4%CF%BD%AC')
# # <a href="/ArticleSearchList.nhn?search.clubid=10912875&amp;search.menuid=&amp;search.searchdate=all&amp;search.searchBy=0&amp;search.sortBy=date&amp;search.option=0&amp;userDisplay=50&amp;search.query=%B9%CC%B4%CF%BD%AC&amp;search.includeAll=&amp;search.exclude=&amp;search.include=&amp;search.exact=">50개씩</a>


# for i in range(1, 11):
#     req = driver.page_source
#     soup = BeautifulSoup(req, 'html.parser')
#     titles = soup.select('#main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr')

#     print(i, '번째 페이지')
#     view_list = []

#     for j, t in enumerate(titles, 1):
#         #main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child(1) > td.td_article > div.board-number > div
#         #main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child(2) > td.td_article > div.board-number > div
#         id = t.select_one(f'#main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child({j}) > td.td_article > div.board-number > div').text
#         #main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child(1) > td.td_article > div.board-list > div > a.article
#         #main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child(2) > td.td_article > div.board-list > div > a.article
#         #main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child(43) > td.td_article > div.board-number > div
#         title = t.select_one(f'#main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child({j}) > td.td_article > div.board-list > div > a.article').text.strip()
#         #main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child(1) > td.td_date
#         #main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child(2) > td.td_date
#         date = t.select_one(f'#main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child({j}) > td.td_date').text.strip()
#         #main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child(1) > td.td_name > div > table > tbody > tr > td > a
#         #main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child(2) > td.td_name > div > table > tbody > tr > td > a
#         writer = t.select_one(f'#main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child({j}) > td.td_name > div > table > tbody > tr > td > a').text.strip()
#         #main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child(1) > td.td_view
#         #main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child(2) > td.td_view
#         view = t.select_one(f'#main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child({j}) > td.td_view').text
        
#         print(id, title, date, writer, view)
#         ws.append([id, title, writer, date, view])

#     # print('range [i]???', i)
#     if i < 9:
#         # i += 1
#         # print('i += 1???', i)
#         driver.find_element(By.XPATH, f'//*[@id="main-area"]/div[7]/a[{i}+1]').click()
#         # print('driver[i]???', i)
#         if i == 10:
#             break

# wb.save('chapter7/20230926 미니쉬.xlsx')
