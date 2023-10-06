from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl

from webdriver_manager.chrome import ChromeDriverManager


keyword = input('검색어를 입력하세요 >>> ')
url = f"https://map.naver.com/p/search/{keyword}/place/33084820?c=15.00,0,0,0,dh&isCorrectAnswer=true"

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

# driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)

# driver.switch_to.frame("cafe_main")

time.sleep(2)

# review = driver.find_element(By.CSS_SELECTOR, '#app-root > div > div > div > div.place_fixed_maintab > div > div > div > div > a:nth-child(2) > span')
review = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[5]/div/div/div/div/a[2]')
review.click()

#app-root > div > div > div > div.place_fixed_maintab > div > div > div > div > a:nth-child(2)
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

i = 1

try:
    while True:
        driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[7]/div[3]/div[3]/div[2]/a').click()
        i += 1
        time.sleep(1)

        # if i == 10:
        #     break
except Exception as e:
    print('---END---')

list = driver.find_elements(By.CSS_SELECTOR, '#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li')

#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child(1)
#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child(2)

for i, l in enumerate(list, 1):
    writer = l.find_element(By.CSS_SELECTOR, 'div.VYGLG').text

    try:            
        # rl = l.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[7]/div[3]/div[3]/div[1]/ul/li[1]/div[1]/a[2]/div[2]/span[1]').text
        rl = l.find_element(By.CSS_SELECTOR, f'#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child({i}) > div.SdWYt > a.QAxJb > div.yu1jg > span:nth-child(1)').text    

        review_len = rl.replace('리뷰', '').strip()
    except:
        review_len = 0

    try:
        comment = l.find_element(By.CSS_SELECTOR, 'span.zPfVt').text
    except:
        comment = '글없음'

    # date = l.find_element(By.XPATH, f'//*[@id="app-root"]/div/div/div/div[7]/div[3]/div[3]/div[1]/ul/li[{i}]/div[3]/div/div[2]/span[1]/span[2]').text
    date = l.find_element(By.CSS_SELECTOR, f'#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child({i}) > div.qM6I7 > div > div._7kR3e > span:nth-child(1) > span:nth-child(3)').text
    # visit = l.find_element(By.XPATH, f'//*[@id="app-root"]/div/div/div/div[7]/div[3]/div[3]/div[1]/ul/li[{i}]/div[3]/div/div[2]/span[2]').text
    visit = l.find_element(By.CSS_SELECTOR, f'#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child({i}) > div.qM6I7 > div > div._7kR3e > span:nth-child(2)').text
    # pay = l.find_element(By.XPATH, f'//*[@id="app-root"]/div/div/div/div[7]/div[3]/div[3]/div[1]/ul/li[{i}]/div[3]/div/div[2]/span[3]').text
    pay = l.find_element(By.CSS_SELECTOR, f'#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child({i}) > div.qM6I7 > div > div._7kR3e > span:nth-child(3)').text

    payment = pay.replace('인증 수단', '').strip()

    # print(writer, review_len, comment, date, visit)

    print(writer, review_len, comment, date, visit, payment)

    # ws.append([writer, review_len, comment, date, visit])
    ws.append([writer, review_len, comment, date, visit, payment])

wb.save(f'chapter7/네이버플레이스_{keyword}.xlsx')


# //*[@id="app-root"]/div/div/div/div[7]/div[3]/div[3]/div[1]/ul/li[1]/div[3]/div/div[2]/span[1]/span[2]
# //*[@id="app-root"]/div/div/div/div[7]/div[3]/div[3]/div[1]/ul/li[2]/div[3]/div/div[2]/span[1]/span[2]

# //*[@id="app-root"]/div/div/div/div[7]/div[3]/div[3]/div[1]/ul/li[84]/div[3]/div/div[2]/span[1]/span[2]
# //*[@id="app-root"]/div/div/div/div[7]/div[3]/div[3]/div[1]/ul/li[87]/div[3]/div/div[2]/span[1]/span[2]


#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child(1) > div.qM6I7 > div > div._7kR3e > span:nth-child(1) > span:nth-child(3)
#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child(2) > div.qM6I7 > div > div._7kR3e > span:nth-child(1) > span:nth-child(3)

#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child(1) > div.qM6I7 > div > div._7kR3e > span:nth-child(2)
#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child(2) > div.qM6I7 > div > div._7kR3e > span:nth-child(2)

#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child(1) > div.qM6I7 > div > div._7kR3e > span:nth-child(3)
#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child(2) > div.qM6I7 > div > div._7kR3e > span:nth-child(3)

#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child(1) > div.SdWYt > a.QAxJb > div.yu1jg > span:nth-child(1)
#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child(2) > div.SdWYt > a.QAxJb > div.yu1jg > span:nth-child(1)


#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child(12) > div.qM6I7 > div > div.Lomxm > div > a
#app-root > div > div > div > div:nth-child(7) > div:nth-child(3) > div.place_section.k5tcc > div.place_section_content > ul > li:nth-child(11) > div.qM6I7 > div > div.Lomxm > a