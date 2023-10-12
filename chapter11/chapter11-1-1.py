from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

keyword = input('검색어를 입력해주세요 >>> ')

url = f'https://map.naver.com/p/search/{keyword}'

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)

time.sleep(2)

driver.switch_to.frame("searchIframe")

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '#_pcmap_list_scroll_container').click()

for i in range(1, 15):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    i += 1
    time.sleep(1)

# while True:
#     driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
#     time.sleep(1)
# execpt:
#     break

cards = driver.find_elements(By.CSS_SELECTOR, 'li.UEzoS.rTjJo')

# .get_attribute('data-laim-exp-id')
# print(test)

for j, card in enumerate(cards, 1):
    c = card.get_attribute('data-laim-exp-id')

    if (c == "undefined*e"):
        pass
    else:
        # print(c)
        store_name = card.find_element(By.CSS_SELECTOR, 'span.place_bluelink,TYaxT').text
        try:
            review_num = card.find_element(By.XPATH, f'//*[@id="_pcmap_list_scroll_container"]/ul/li[{j}]/div[1]/div[2]/div/span[2]/text()').text
        except:
            review_num = '평점 없음'

        print(store_name, review_num)

# //*[@id="_pcmap_list_scroll_container"]/ul/li[6]/div[1]/div[2]/div/span[2]/span

# //*[@id="_pcmap_list_scroll_container"]/ul/li[6]/div[1]/div[2]/div/span[2]/text()

# //*[@id="_pcmap_list_scroll_container"]/ul/li[6]/div[1]/div[2]/div/span[2]

# //*[@id="_pcmap_list_scroll_container"]/ul/li[7]/div[1]/div/div/span[2]

# i = 1

# try:
    # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
#     i += 1
#     time.sleep(1)
# except:
#     print('----END----')

# i = 1


