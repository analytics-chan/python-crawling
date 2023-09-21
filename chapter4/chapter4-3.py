# 네이버 뉴스 본문 링크 가져오기
# 네이버 검색시 네이버 뉴스만 붙어있는 기사 추출

import requests
from bs4 import BeautifulSoup
import time
# import pyautogui

# 검색어 가져오기
keyword = input('검색어를 입력하세요 >>> ')
# keyword = pyautogui.prompt('검색어를 입력하세요')

response = requests.get(f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}')
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# 뉴스 기사 div 10개 추출
articles = soup.select('div.info_group')

for a in articles:
    # 리스트
    links = a.select('a.info')
    # print(links)
    # 링크가 2개 이상이면
    if len(links) >= 2:
        # 두번째 링크의 href를 추출
        url = links[1].attrs['href']
        # print(url)

        # requests 다시 보내기
        response = requests.get(url)
        # response = requests.get(url, headers={'User-agent': 'Mozila/5.0'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        
        # 연예 뉴스
        if "entertain" in response.url:
            title = soup.select_one('.end_tit')
            content = soup.select_one('#articeBody')
        # 스포츠 뉴스
        elif "sports" in response.url:
            title = soup.select_one('h4.title')
            content = soup.select_one('#newsEndContents')

            # 본문 내용 안에 불필요한 div, p 삭제
            divs = content.select('div')

            for div in divs:
                div.decompose()
            
            paragraph = content.select('p')

            for p in paragraph:
                p.decompose()

        # 일반 뉴스
        else:
            title = soup.select_one('#title_area > span')
            content = soup.select_one('#dic_area')
        
        print('---링크---\n', url)
        print('---제목---\n', title.text.strip())
        print('---본문---\n', content.text.strip())
        time.sleep(0.3)