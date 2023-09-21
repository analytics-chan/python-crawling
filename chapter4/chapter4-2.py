# 네이버 뉴스 본문 링크 가져오기
# 네이버 검색시 네이버 뉴스만 붙어있는 기사 추출

import requests
from bs4 import BeautifulSoup

response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90')
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
        print(url)