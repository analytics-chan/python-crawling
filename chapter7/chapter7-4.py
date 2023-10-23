from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl
import datetime

today = datetime.datetime.today()
year = str(today.year)
month = str(today.month)
day = str(today.day)

keyword = input('[블랙키위] 검색어를 입력해주세요 >>> ')
blackKiwiURL = f"https://blackkiwi.net/service/keyword-analysis?keyword={keyword}&platform=naver"

wb = openpyxl.Workbook()

ws = wb.create_sheet(keyword, 0)

ws.append(['순위', '제목', '링크', '키워드'])

ws.column_dimensions['B'].width = 50
ws.column_dimensions['C'].width = 30
ws.column_dimensions['D'].width = 25

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(blackKiwiURL)

time.sleep(20)

driver.find_element(By.CSS_SELECTOR, '#root > main > div.style__KeywordAnalysisHeader-sc-10xntpe-0.dcLXkO > div > div.style__Tab-sc-qvfki9-0.djRbPw.style__TopTab-sc-10xntpe-3.fwjzGs > div:nth-child(2)').click()

keyword_box = driver.find_elements(By.CSS_SELECTOR, '#root > main > div.style__Page-sc-1da7kpf-2.edyeyw > div.style__PageInnerWrapper-sc-1da7kpf-3.eyvNrG.bodyInnerWrapper > div.style__RefContainer-sc-q2l2qb-0.iSiLKY > div > div > div > div.style__Body-sc-1sb1qkf-6.dZDueT > div.style__GenericTable-sc-302yz3-0.jsdQar > div.style__BottomTableWrapper-sc-302yz3-2.cGYxAy.bottomTable > table > tbody > tr')
#root > main > div.style__Page-sc-1da7kpf-2.edyeyw > div.style__PageInnerWrapper-sc-1da7kpf-3.eyvNrG.bodyInnerWrapper > div.style__RefContainer-sc-q2l2qb-0.iSiLKY > div > div > div > div.style__Body-sc-1sb1qkf-6.dZDueT > div.style__GenericTable-sc-302yz3-0.jsdQar > div.style__BottomTableWrapper-sc-302yz3-2.cGYxAy.bottomTable > table > tbody > tr:nth-child(1)
#root > main > div.style__Page-sc-1da7kpf-2.edyeyw > div.style__PageInnerWrapper-sc-1da7kpf-3.eyvNrG.bodyInnerWrapper > div.style__RefContainer-sc-q2l2qb-0.iSiLKY > div > div > div > div.style__Body-sc-1sb1qkf-6.dZDueT > div.style__GenericTable-sc-302yz3-0.jsdQar > div.style__BottomTableWrapper-sc-302yz3-2.cGYxAy.bottomTable > table > tbody > tr:nth-child(2)

# print(len(keyword_box))

key_text_box = []

for k in keyword_box:
    key_text = k.find_element(By.CSS_SELECTOR, 'span.ckJCVX > a').text
    key_text_box.append(key_text)

# print(key_text_box)

rank = 1

for i in range (0, len(key_text_box), 1):
    naverURL = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={key_text_box[i]}"
    print(key_text_box[i])

    driver.get(naverURL)

    powerlink_box = driver.find_elements(By.CSS_SELECTOR, '#power_link_body > ul > li')

    for p in powerlink_box:
        link = p.find_element(By.CSS_SELECTOR, 'a.lnk_url').text
        title = p.find_element(By.CSS_SELECTOR, 'a.lnk_head > span:nth-child(1)').text

        print(link, title)
        ws.append([rank, title, link, key_text_box[i]])
        rank += 1
    
    rank = 1

#power_link_body > ul > li.lst.type_more.type_subtitle.ext_link.type_img > div > div.title_url_area > div > a.lnk_url

#power_link_body > ul > li:nth-child(1)
#power_link_body > ul > li:nth-child(2)

wb.save(f'chapter7/{year}{month}{day} {keyword}.xlsx')