from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import openpyxl

# webdriver 설치 및 로딩
options = Options()
options.add_experimental_option('detach',True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service, options = options)

driver.maximize_window()

wb = openpyxl.Workbook()

ws = wb.create_sheet('카페 크롤링', 0)

ws.append(['제목', '내용'])

# 네이버 로그인
# driver.get('https://nid.naver.com/nidlogin.login?mode=number&url=https%3A%2F%2Fwww.naver.com%2F&locale=ko_KR&svctype=1')
# time.sleep(10)

# 웹사이트 접속
driver.get('https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=13764661&search.menuid=865&search.searchdate=all&search.searchBy=1&search.sortBy=date&search.option=0&userDisplay=5&search.query=%BA%B8%C7%E8&search.includeAll=&search.exclude=&search.include=&search.exact=')
time.sleep(3)

title_all = []
article_all = []

# for page in range(1, 3):
for j in range(2, 4):
    print(j - 1, '페이지----------------')

    for i in range(1, 6):
        driver.switch_to.frame("cafe_main")
        
        print('1번째 i >>> ', i)

        # 게시물 클릭
        driver.find_element(By.XPATH, f'//*[@id="main-area"]/div[5]/table/tbody/tr[{i}]/td[1]/div[2]/div/a[1]').click()
        time.sleep(2)

        # 제목 및 게시글 가져오기
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')
        title = soup.select_one('#app > div > div > div.ArticleContentBox > div.article_header > div.ArticleTitle > div > h3').text
        print(title)
        articles = soup.select('#app > div > div > div.ArticleContentBox > div.article_container > div.article_viewer > div:nth-child(2) > div.content.CafeViewer')

        for article in articles:
            article_n = article.get_text().strip()
            article_n = article_n.replace(u'\u200b', u'')
            article_all.append(article_n)
        title_all.append(title)
        print(title_all)
        print(article_all)

        ws.append([title, article_n])

        # 뒤로가기
        driver.back()
        time.sleep(2)

    driver.switch_to.default_content()

    # print('j??? ', j)
    # print('j%10 ??? ', j%10)

    driver.switch_to.frame("cafe_main")

    try:
        if j%10 == 1:
            driver.find_element(By.CLASS_NAME, 'pgR').click()
        else:
            driver.find_element(By.XPATH, f'//*[@id="main-area"]/div[7]/a[{j}]').click()
            # driver.find_element(By.LINK_TEXT, str(j)).click()
    except Exception as e:
        print('----END----')
        break

    driver.switch_to.default_content()

print(title_all)
print(article_all)
# driver.quit()

wb.save('chapter7/네이버카페 크롤링.xlsx')