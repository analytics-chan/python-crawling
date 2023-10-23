# 구글 플레이스토어 리뷰 크롤링
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

keyword = input('검색어를 입력해주세요 >>> ')
url = f'https://play.google.com/store/search?q={keyword}&c=apps&hl=ko-KR'

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

# review_box = driver.find_element(By.CSS_SELECTOR, 'div.odk6He')
review_box = driver.find_element(By.CSS_SELECTOR, 'div.fysCi')
# review_box = driver.find_element(By.CSS_SELECTOR, '#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.HQdjr.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div > div > div > div.fysCi > div > div:nth-child(2)')
# review_box = driver.find_element(By.CSS_SELECTOR, 'div.jgIq1')

# div.jgIq1
# div.RHo1pe

# driver.find_element(By.CSS_SELECTOR, 'div.fysCi').send_keys(Keys.PAGE_DOWN)

driver.execute_script('arguments[0].scrollBy(0, 10000)', review_box)
# 10000까지 80개

# driver.execute_script('arguments[0].scrollIntoView(true)', review_box)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

reviews = driver.find_elements(By.CSS_SELECTOR, 'div.RHo1pe')

# res = driver.page_source
# soup = BeautifulSoup(res, 'html.parser')

# reviews = soup.select('div.RHo1pe')

for review in reviews:
    # writer = review.select_one('div.X5PpBb').text
    # star = review.select_one('div.iXRFPc').attrs['aria-label']
    # date = review.select_one('span.bp9Aid').text
    # comment = review.select_one('div.h3YV2d').text
    # useful = review.select_one('div.AJTPZc').text

    writer = review.find_element(By.CSS_SELECTOR, 'div.X5PpBb').text
    star = review.find_element(By.CSS_SELECTOR, 'div.iXRFPc').get_attribute('aria-label')
    date = review.find_element(By.CSS_SELECTOR, 'span.bp9Aid').text
    comment = review.find_element(By.CSS_SELECTOR, 'div.h3YV2d').text
    useful = review.find_element(By.CSS_SELECTOR, 'div.AJTPZc').text

    time.sleep(1)

    print(writer, star, date, comment, useful)