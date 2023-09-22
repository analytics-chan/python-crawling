# 워드 클라우드

import requests
from bs4 import BeautifulSoup
import time
import pyperclip
import pyautogui

# 검색어 가져오기
keyword = input('검색어를 입력하세요 >>> ')

# 여러 페이지 추출
lastPage = int(input('몇 페이지까지 추출하시겠습니까?'))

# 본문 전체 내용
total_content = ''

# 기사 갯수
article_num = 0

page_num = 1

for i in range(1, lastPage * 10, 10):
    # page = document.add_paragraph(f'{page_num}페이지')
    # page.font_name = "돋움"

    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={keyword}&start={i}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.select('div.info_group')

    for a in articles:
        links = a.select('a.info')

        if len(links) >= 2:
            url = links[1].attrs['href']

            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            if 'entertain' in response.url:
                content = soup.select_one('#articeBody')
            elif 'sports' in response.url:
                content = soup.select_one('#newsEndContents')

                divs = content.select('div')
                
                for div in divs:
                    div.decompose()

                paras = content.select('p')

                for para in paras:
                    para.decompose()
            else:
                content = soup.select_one('#dic_area')

            print('-----본문-----\n', content.text.strip())
            total_content += content.text.strip()
            article_num += 1
            time.sleep(0.3)
        
    page_num += 1

print(f"{article_num}개 기사 크롤링 완료")
pyperclip.copy(total_content)
pyautogui.alert('클립보드에 복사되었습니다.')