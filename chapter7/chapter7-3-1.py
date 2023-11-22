from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

import time
import openpyxl

# keyword = input('검색어를 입력하세요 >>> ')
keyword = "더와이즈치과병원"

url = f"https://map.naver.com/p/search/{keyword}"
# url = f"https://map.naver.com/p/search/{keyword}/place/33084820?c=15.00,0,0,0,dh&isCorrectAnswer=true"

wb = openpyxl.Workbook()
ws = wb.create_sheet(keyword, 0)

ws.column_dimensions['A'].width = 15
ws.column_dimensions['B'].width = 12
ws.column_dimensions['C'].width = 70
ws.column_dimensions['D'].width = 25
ws.column_dimensions['E'].width = 15

ws.append(['작성자', '작성 리뷰수', '작성리뷰', '날짜', '방문수', '인증 수단'])

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)

# driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)

driver.switch_to.frame("entryIframe")

#iframe 밖으로 나오기
#browser.switch_to.default_content()

# driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)

time.sleep(2)
# review = driver.find_element(By.CSS_SELECTOR, '#app-root > div > div > div > div.place_fixed_maintab > div > div > div > div > a:nth-child(2) > span')
review = driver.find_element(By.CSS_SELECTOR, '#app-root > div > div > div > div.place_fixed_maintab > div > div > div > div > a:nth-child(2)')
# review = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[5]/div/div/div/div/a[2]')
review.click()

lis = driver.find_elements(By.CSS_SELECTOR, 'li.YeINN')
before_len = len(lis)
print(before_len)

#app-root > div > div > div > div.place_fixed_maintab > div > div > div > div > a:nth-child(2)

# i = 1

try:
    while True:
        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)

        time.sleep(1)
        
        # driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[6]/div[3]/div[3]/div[2]/a').click()
        driver.find_element(By.CSS_SELECTOR, '#app-root > div > div > div > div:nth-child(6) > div:nth-child(3) > div.place_section.k5tcc > div.NSTUp > div > a > span').click()

        lis = driver.find_elements(By.CSS_SELECTOR, 'li.YeINN')
        after_len = len(lis)
        print(after_len)
        
        time.sleep(1)

        if after_len == 10:
            break

        # if before_len == after_len:
        #     break

        # before_len = after_len

        # if i == 10:
        #     break
except Exception as e:
    print('---END---')

# res = driver.page_source
# soup = BeautifulSoup(res, 'html.parser')

try:
    review_list = driver.find_elements(By.CSS_SELECTOR, 'li.YeINN')
    
    print('총 리뷰 수 : ', len(review_list))

    for review in review_list:
        try:
            # find_review = review.find('div.ZZ4OK > a > span.rvCSr > svg')
            # print(find_review)
            more_content = review.find_element(By.CSS_SELECTOR, 'div.ZZ4OK > a > span.rvCSr > svg')
            print(more_content)
            more_content.click()
            time.sleep(1)

            user_review = review.find_element(By.CSS_SELECTOR, 'div.ZZ4OK > a > span.zPfVt')
        except:
            user_review = review.find_element(By.CSS_SELECTOR, 'div.ZZ4OK > a > span.zPfVt')

            time.sleep(1)
except:
    time.sleep(1)
    print('리뷰가 존재하지 않음')




# # driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)

# reviews_s = driver.find_elements(By.CSS_SELECTOR, 'li.YeINN')
# # print(len(reviews))

# driver.find_element(By. CSS_SELECTOR, '#app-root > div > div > div > div:nth-child(6) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child(4) > div.ZZ4OK > a > span.rvCSr').click()
# # print(len(etc))
# # print(etc)

# #app-root > div > div > div > div:nth-child(6) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child(4) > div.ZZ4OK > a > span.rvCSr

# time.sleep(1)

# # try:
# #     for e in etc:
# #         e.click()
# # except:
# #     pass

# # for s in reviews_s:
# #     span_len = s.find_elements(By.CSS_SELECTOR, 'a.xHaT3 > span')
# #     print(len(span_len))

# #     try:
# #         s.find_element(By. CSS_SELECTOR, 'a.xHaT3 > span:nth-child(2) > svg > path').click()
# #     except:
# #         pass

#     # if len(span_len) == 2:
#     #     s.find_element(By. CSS_SELECTOR, 'a.xHaT3 > span:nth-child(2) > svg > path').click()
#     # else:
#     #     pass

    
#     # try:
#     #     # etc = driver.find_element(By. CSS_SELECTOR, 'span.rvCSr')
#     #     # etc.click()
#     #     driver.find_element(By. CSS_SELECTOR, 'span.rvCSr').click()

#     #     etc = driver.find_element(By. CSS_SELECTOR, 'span.rvCSr')
        

#     #     time.sleep(1)

#     #     print('클릭완료')
#     # except:
#     #     pass
#     #     print('pass')

# # etc = driver.find_elements(By.CSS_SELECTOR, 'span.rvCSr > svg')
# # print(len(etc))

# # for e in etc:
# #     e.click()

# # res = driver.page_source
# # soup = BeautifulSoup(res, 'html.parser')

# # reviews = soup.select('li.YeINN')
# # print(len(reviews))

# # for r in reviews:

# #     try:
# #         etc = driver.find_element(By. CSS_SELECTOR, 'span.rvCSr')
# #         etc.click()
        
# #         time.sleep(1)

# #         print('클릭완료')

# #     except:
# #         pass
# #         print('패스')

# #     time.sleep(1)

# #     nick = r.select_one('div.VYGLG').text

# #     print(nick)









#     # etc = r.find_element(By.CSS_SELECTOR, 'span.rvCSr')

#     # print(bool(etc))
    
#     # etc.click()

#     # etc = driver.find_element(By.CSS_SELECTOR, 'span.rvCSr > svg').click()
#     # print(len(etc))

#     # for e in etc:
#     #     e.click()
