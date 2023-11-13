# 네이버 쇼핑 검색, 연관검색어
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import os
import time
import datetime
from openpyxl import Workbook, load_workbook
import requests

today = datetime.datetime.today()
year = str(today.year)
month = str(today.month)
day = str(today.day)

url = "https://shopping.naver.com/home"

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)


input_query = driver.find_element(By.CSS_SELECTOR, 'input._searchInput_search_text_3CUDs')
input_query.click()

# input_query.clear()

time.sleep(1)

input_query.send_keys('네스프레소')

key_box = driver.find_elements(By.CSS_SELECTOR, 'div._autoComplete_basis_result_1cDj8._autoComplete_active_3_pom > div > ul')
print(len(key_box))

print('----- 검색창 연관검색어 -----')

time.sleep(1)

if len(key_box) != 0:
    for i in range(0, len(key_box)):
        # print(key_box[i])
        print(key_box[i].get_attribute('class'))

        if key_box[i].get_attribute('class') == "":
            # _autoComplete_list_brandstore_1uJCB
            print(key_box[i].get_attribute('class'))
            lis = key_box[i].find_elements(By.CSS_SELECTOR, f'#gnb-gnb > div._gnb_header_area_150KE > div > div._gnbLogo_gnb_logo_3eIAf > div > div._gnbSearch_gnb_search_3O1L2 > form > div._gnbSearch_inner_2Zksb > div:nth-child(2) > div > div._autoComplete_basis_result_1cDj8._autoComplete_active_3_pom > div > ul:nth-child({i}) > li')
            print(len(lis))

            # for l in lis:
            #     try:
            #         title = l.find_element(By.CSS_SELECTOR, 'em').text
            #             # print(title)
            #     except:
            #         title = l.find_element(By.CSS_SELECTOR, 'li > a').text
            #             # print(title)
                
            # print(title)

        else:
            pass


        
else:
    print('검색창 내 연관검색어가 없습니다.')

time.sleep(1)

search = driver.find_element(By.CSS_SELECTOR, 'button._searchInput_button_search_1n1aw')
search.click()

time.sleep(1)

shopping_keyword = driver.find_elements(By.CSS_SELECTOR, '#container > div.relatedTags_relation_tag__Ct0q2 > div > ul > li')
print(len(shopping_keyword))

if len(shopping_keyword) != 0:
    etc_btn = driver.find_element(By.CSS_SELECTOR, 'button.relatedTags_btn_more__Fdsm1')
    etc_btn.click()

    time.sleep(1)

    print('----- 쇼핑연관 검색어 -----')

    for s in shopping_keyword:
        shop_title = s.find_element(By.CSS_SELECTOR, 'li > a').text

        print(shop_title)
else:
    print('연관 검색어가 없습니다.')

time.sleep(1)

print(f'----- {today.now()} 크롤링 종료 -----')

### 코드 수정 필요함