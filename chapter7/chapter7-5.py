# 구글 플레이스토어 리뷰 크롤링
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import openpyxl
import re
from datetime import datetime

today = datetime.today()
year = str(today.year)
month = str(today.month)
day = str(today.day)
file_date = year + month + day

keyword = input('검색어를 입력해주세요 >>> ')
url = f'https://play.google.com/store/search?q={keyword}&c=apps&hl=ko-KR'

wb = openpyxl.Workbook()
ws = wb.create_sheet(keyword, 0)

ws.column_dimensions['A'].width = 18
ws.column_dimensions['B'].width = 15
ws.column_dimensions['D'].width = 10
ws.column_dimensions['E'].width = 70

ws.append(['Crawling-Date', 'Nickname', 'Star', 'Create-Date', 'Comment', 'Useful'])

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)

driver.find_element(By.CSS_SELECTOR, 'a.Qfxief').click()

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '#yDmH0d > c-wiz.SSPGKf.Czez9d > div > div > div.tU8Y5c > div.wkMJlb.YWi3ub > div > div.qZmL0 > div:nth-child(1) > c-wiz:nth-child(4) > section > div > div.Jwxk6d > div:nth-child(5) > div > div > button > span').click()

time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="sortBy_1"]/div[2]').click()

time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[5]/div[2]/div/div/div/div/div[2]/div[2]/div/div/span[2]/div[2]').click()

time.sleep(2)

# review_box = driver.find_element(By.CSS_SELECTOR, 'div.odk6He')
review_box = driver.find_element(By.CSS_SELECTOR, 'div.fysCi')
# review_box = driver.find_element(By.CSS_SELECTOR, '#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.HQdjr.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div > div > div > div.fysCi > div > div:nth-child(2)')
# review_box = driver.find_element(By.CSS_SELECTOR, 'div.jgIq1')

# div.jgIq1
# div.RHo1pe

# driver.find_element(By.CSS_SELECTOR, 'div.fysCi').send_keys(Keys.PAGE_DOWN)

# driver.execute_script('arguments[0].scrollBy(0, 20000)', review_box)
# 10000까지 80개

# time.sleep(2)

# driver.execute_script('arguments[0].scrollIntoView(true)', review_box)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

while True:

    driver.execute_script('arguments[0].scrollBy(0, 40000)', review_box)

    time.sleep(2)

    reviews = driver.find_elements(By.CSS_SELECTOR, 'div.RHo1pe')

    print(len(reviews))

    try:
        if len(reviews) >= 10000:
            break
    except Exception as e:
        print('-----END-----')
        break

res = driver.page_source
soup = BeautifulSoup(res, 'html.parser')

reviews = soup.select('div.RHo1pe')

for i, review in enumerate(reviews, 1):
    # bs4 version
    writer = review.select_one('div.X5PpBb').text
    star = review.select_one('div.iXRFPc').attrs['aria-label']
    date = review.select_one('span.bp9Aid').text

    try:
        comment = review.select_one('div.h3YV2d').text
    except:
        comment = ""
        
    try:
        useful = review.select_one('div.AJTPZc').text
        
        patten = "사용자 ([0-9]+)명이 이 리뷰가 유용하다고 평가함"
        useful_result = re.sub(r'[^0-9]', '', useful)
    except:
        useful_result = 0

    # # 데이터 전처리 version_1
    # if '년 ' and '월 ' and '일' in date:
    #     date = date.replace('년 ', '-')
    #     date = date.replace('월 ', '-')
    #     date = date.replace('일', '')

    # 데이터 전처리 version_2
    yy = date.split('년')[0].strip()
    mm = date.split('년')[1].split('월')[0].strip()
    dd = date.split('년')[1].split('월')[1][:-1].strip()
    
    if len(mm) == 1:
        mm = '0' + mm

    if len(dd) ==1:
        dd = '0' + dd

    # print(f'{yy}-{mm}-{dd}')

    date_result = f'{yy}-{mm}-{dd}'

    # # selenium version
    # writer = review.find_element(By.CSS_SELECTOR, 'div.X5PpBb').text
    # star = review.find_element(By.CSS_SELECTOR, 'div.iXRFPc').get_attribute('aria-label')
    # date = review.find_element(By.CSS_SELECTOR, 'span.bp9Aid').text

    # try:
    #     comment = review.find_element(By.CSS_SELECTOR, 'div.h3YV2d').text
    # except:
    #     comment = ""

    # try:
    #     useful = review.find_element(By.CSS_SELECTOR, 'div.AJTPZc').text

    #     patten = "사용자 ([0-9]+)명이 이 리뷰가 유용하다고 평가함"
    #     useful_result = re.sub(r'[^0-9]', '', useful)
    # except:
    #     useful_result = 0

    # if '년 ' and '월 ' and '일' in date:
    #     date = date.replace('년 ', '-')
    #     date = date.replace('월 ', '-')
    #     date = date.replace('일', '')
   
    star_result = re.sub(r'[^0-9]', '', star)[1:]

    # time.sleep(1)

    print(i, writer, int(star_result), date_result, comment, int(useful_result))
    ws.append([str(today)[:-7], writer, int(star_result), date_result, comment, int(useful_result)])


wb.save(f'chapter7/{file_date} {keyword}.xlsx')