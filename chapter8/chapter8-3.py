# 구글 이미지 크롤링 및 큰 이미지 다운로드
# click_intercepted Error 해결

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 시간차 처리
import time

# 폴더 생성
import os

# 파일 저장
import urllib.request

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

keyword = input('검색어를 입력해주세요 >>> ')

if not os.path.exists(f'chapter8/{keyword}'):
    os.mkdir(f'chapter8/{keyword}')

url = f"https://www.google.com/search?sca_esv=568723682&hl=ko&sxsrf=AM9HkKmVilDIuKnlc4pOE-SLOJjz5pPRbw:1695788470987&q={keyword}&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiso7Wr-MmBAxXzk1YBHQ-cC7sQ0pQJegQICxAB&biw=2560&bih=1283&dpr=1"

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

# 불필요한 에러 메시지 삭제
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get(url)

before_h = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    time.sleep(2)

    after_h = driver.execute_script('return document.body.scrollHeight')

    if after_h == before_h:
        break
    before_h = after_h

# 썸네일 이미지 추출
imgs = driver.find_elements(By.CSS_SELECTOR, '.rg_i.Q4LuWd')

for i, img in enumerate(imgs, 1):
    # 이미지 클릭 후 큰 사이즈 추출
    # 클릭하다보면 element click intercepted Error 발생

    # JavaScript로 클릭을 직접 하도록 만들어서 해결
    driver.execute_script('arguments[0].click();', img)

    # 셀레니움으로 직접 클릭
    # img.click()

    time.sleep(1)

    # 큰 이미지 주소 추출
    # imgUrl = driver.find_element(By.CSS_SELECTOR, '.r48jcc.pT0Scc').get_attribute('src')
    # imgUrl = driver.find_element(By.CSS_SELECTOR, '.r48jcc.pT0Scc.iPVvYb').get_attribute('src')
    # print(i, imgUrl)

    # if not imgUrl:
    #     imgUrl = driver.find_element(By.CSS_SELECTOR, '.r48jcc.pT0Scc').get_attribute('src')
    #     print(i, imgUrl)
    
    # 이미지 url 주소 에러 방지
    try:
        imgUrl = driver.find_element(By.CSS_SELECTOR, '.r48jcc.pT0Scc.iPVvYb').get_attribute('src')
    except:
        imgUrl = driver.find_element(By.CSS_SELECTOR, '.r48jcc.pT0Scc').get_attribute('src')

    # 이미지 다운로드
    # HTTP Error 403: Forbidden 에러
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    # 이미지 다운로드 시 오류나는 이미지 제외하고 저장
    try:
        urllib.request.urlretrieve(imgUrl, f'chapter8/{keyword}/{i}.jpg')
    except:
        pass

    # 50개까지만 저장
    if i == 50:
        break
