# 틱톡 쇼츠
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

import time
import datetime
import os
from openpyxl import Workbook, load_workbook

today = datetime.datetime.today()
year = str(today.year)
month = str(today.month)
day = str(today.day)

if len(month) == 1:
    month = '0' + month

if len(day) == 1:
    day = '0' + day

path = '02.sns_shorts'
file_list = os.listdir(path)
file_name = f'{year}{month}{day} tictok_shorts.xlsx'

if file_name in file_list:
    wb = load_workbook(os.path.join(path, file_name))
else:
    wb = Workbook()

    ws = wb.create_sheet('tictok', 0)

ws = wb.active

ws['A1'] = 'Date'
ws['B1'] = '계정ID'
ws['C1'] = '내용'
ws['D1'] = '작성일자'
ws['E1'] = '좋아요'
ws['F1'] = '댓글수'
ws['G1'] = '저장수'
ws['H1'] = '링크'

ws.column_dimensions['A'].width = 20
ws.column_dimensions['B'].width = 15
ws.column_dimensions['C'].width = 50
ws.column_dimensions['D'].width = 12
ws.column_dimensions['F'].width = 12

url = "https://www.tiktok.com/foryou"

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)

gue = driver.find_element(By.CSS_SELECTOR, '#loginContainer > div > div > div.css-txolmk-DivGuestModeContainer.exd0a435 > div > div > div > div > div')

time.sleep(1)

gue.click()


# test_1
# shorts = driver.find_elements(By.CSS_SELECTOR, '#main-content-homepage_hot > div.css-9fq6q2-DivOneColumnContainer.e108hwin0 > div')
# print(len(shorts))

#loginContainer > div > div > div.css-txolmk-DivGuestModeContainer.exd0a435 > div > div > div > div > div
#loginContainer > div > div > div.css-txolmk-DivGuestModeContainer.exd0a435 > div > div.css-u3m0da-DivBoxContainer.e1cgu1qo0 > div > div > div

# for s in shorts:
#     id = s.find_element(By.CSS_SELECTOR, 'a.emt6k1z1.css-1ew4g6u-StyledLink-StyledAuthorAnchor.er1vbsz0 > h3').text
#     link = s.find_element(By.CSS_SELECTOR, 'a.emt6k1z1.css-1ew4g6u-StyledLink-StyledAuthorAnchor.er1vbsz0').get_attribute('href')

#     print(id, link)

#main-content-homepage_hot > div.css-9fq6q2-DivOneColumnContainer.e108hwin0 > div:nth-child(1) > div > div.css-1hhj6ie-DivTextInfoContainer.etvrc4k7 > div.css-1mnwhn0-DivAuthorContainer.etvrc4k6 > a.emt6k1z1.css-1ew4g6u-StyledLink-StyledAuthorAnchor.er1vbsz0 > h3
#main-content-homepage_hot > div.css-9fq6q2-DivOneColumnContainer.e108hwin0 > div:nth-child(2) > div > div.css-1hhj6ie-DivTextInfoContainer.etvrc4k7 > div.css-1mnwhn0-DivAuthorContainer.etvrc4k6 > a.emt6k1z1.css-1ew4g6u-StyledLink-StyledAuthorAnchor.er1vbsz0 > h3
    
#main-content-homepage_hot > div.css-9fq6q2-DivOneColumnContainer.e108hwin0 > div:nth-child(1) > div > div.css-1hhj6ie-DivTextInfoContainer.etvrc4k7 > div.css-1mnwhn0-DivAuthorContainer.etvrc4k6 > a.emt6k1z1.css-1ew4g6u-StyledLink-StyledAuthorAnchor.er1vbsz0
#main-content-homepage_hot > div.css-9fq6q2-DivOneColumnContainer.e108hwin0 > div:nth-child(2) > div > div.css-1hhj6ie-DivTextInfoContainer.etvrc4k7 > div.css-1mnwhn0-DivAuthorContainer.etvrc4k6 > a.emt6k1z1.css-1ew4g6u-StyledLink-StyledAuthorAnchor.er1vbsz0

# test_2

#xgwrapper-0-7302336016243838251 > video

time.sleep(2)

vi = driver.find_element(By.CSS_SELECTOR, 'div.e1yey0rl2 > div > video')

vi.click()

time.sleep(1)

def info():
    id = driver.find_element(By.CSS_SELECTOR, 'span.css-1c7urt-SpanUniqueId.evv7pft1 > span').text
    # print(id)

    content = driver.find_element(By.CSS_SELECTOR, 'div.e1mecfx01').text

    wr_date = driver.find_element(By.CSS_SELECTOR, 'span.evv7pft3 > span:nth-child(3)').text

    like = driver.find_element(By.CSS_SELECTOR, 'div.ehlq8k31 > button:nth-child(1) > strong.e1hk3hf92').text

    save = driver.find_element(By.CSS_SELECTOR, 'div.ehlq8k31 > button:nth-child(3) > strong.e1hk3hf92').text

    review_count = driver.find_element(By.CSS_SELECTOR, 'div.e1aa9wve2').text

    link = driver.find_element(By.CSS_SELECTOR, 'div.ehlq8k33 > p.ehlq8k34').text


    print(id, content, wr_date, like, review_count[4:-1], save, link)
    ws.append([today.now(), id, content, wr_date, like, int(review_count[4:-1]), save, link])

#app > div.css-14dcx2q-DivBodyContainer.e1irlpdw0 > div:nth-child(4) > div > div.css-1qjw4dg-DivContentContainer.e1mecfx00 > div.css-13if7zh-DivCommentContainer.ekjxngi0 > div > div.css-1xlna7p-DivProfileWrapper.ekjxngi4 > div.css-pcqxr7-DivDescriptionContentWrapper.e1mecfx011 > div.css-85dfh6-DivInfoContainer.evv7pft0 > a.evv7pft4.css-n2qh4e-StyledLink-StyledLink.er1vbsz0 > span.css-1c7urt-SpanUniqueId.evv7pft1 > span
#app > div.css-14dcx2q-DivBodyContainer.e1irlpdw0 > div:nth-child(4) > div > div.css-1qjw4dg-DivContentContainer.e1mecfx00 > div.css-13if7zh-DivCommentContainer.ekjxngi0 > div > div.css-1xlna7p-DivProfileWrapper.ekjxngi4 > div.css-pcqxr7-DivDescriptionContentWrapper.e1mecfx011 > div.css-85dfh6-DivInfoContainer.evv7pft0 > a.evv7pft4.css-n2qh4e-StyledLink-StyledLink.er1vbsz0 > span.css-1c7urt-SpanUniqueId.evv7pft1 > span

time.sleep(5)

info()

i = 0

while True:
    next = driver.find_element(By.CSS_SELECTOR, 'div.e11s2kul24 > button:nth-child(8)')

    next.click()

    time.sleep(2)

    info()

    i += 1

    time.sleep(2)

    print('i는 몇번째? >>> ', i)

    if i >= 10:
        break

wb.save(os.path.join(path, file_name))