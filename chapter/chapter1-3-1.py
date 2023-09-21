import requests
from bs4 import BeautifulSoup

response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90')
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select('.news_tit') # 결과는 리스트
# print(links)

for link in links:
  title = link.text # 태그 안에 텍스트 요소만 추출
  url = link.attrs['href'] # 태그 안에 링크 속성 추출
  print(title, url)