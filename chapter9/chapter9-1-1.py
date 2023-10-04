from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

import openpyxl

keyword = input('검색어를 입력하세요 >>> ')

url = f'https://www.youtube.com/results?search_query={keyword}'

wb = openpyxl.Workbook()
ws = wb.create_sheet(keyword, 0)
ws.append(['번호', '작성자', '타이틀', '조회수', '날짜'])

ws.column_dimensions['B'].width = 35
ws.column_dimensions['C'].width = 80

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)

before_h = driver.execute_script('return document.documentElement.scrollHeight')
print(before_h)

while True:
    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight)')

    time.sleep(1)

    after_h = driver.execute_script('return document.documentElement.scrollHeight')

    if after_h == before_h:
        break
    before_h = after_h

    if after_h > 50000:
        break
    
    print(after_h)

# views = driver.find_elements(By.CSS_SELECTOR, '.text-wrapper.style-scope.ytd-video-renderer')

# for i, view in enumerate(views, 1):
#     writer = driver.find_element(By.CSS_SELECTOR, '.yt-simple-endpoint.style-scope.yt-formatted-string').text
#     print(i, writer)

res = driver.page_source
soup = BeautifulSoup(res, 'html.parser')

cards = soup.select('.text-wrapper.style-scope.ytd-video-renderer')

for i, card in enumerate(cards, 1):
    writer = card.select_one('.yt-simple-endpoint.style-scope.yt-formatted-string').text
    title = card.select_one('#video-title > yt-formatted-string').text
    view = card.select_one('#metadata-line > span:nth-child(3)').text[3:-1]
    date = card.select_one('#metadata-line > span:nth-child(4)').text
    # print(writer, title, view, date)

    # if view.find('만'):
    #     view_v2 = view.replace('만', '0000')
    # elif view.find('천'):
    #     view_v2 = view.replace('천', '000')
    # else:
    #     view_v2 = view

    ws.append([i, writer, title, view, date])

wb.save(f'chapter9/유튜브크롤링_{keyword}.xlsx')