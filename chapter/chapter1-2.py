import requests
from bs4 import BeautifulSoup

### 예제
# soup = Beautifulsoup(html, 'html.parser')
# word = soup.select_one('#NM_set_home_btn')
# print

# 사이트 서버에 대화를 시도
response = requests.get('https://play.google.com/store/apps/details?id=com.starbucks.co&hl=ko-KR')

# 사이트에서 html을 가져옴
html = response.text

# html 번역
soup = BeautifulSoup(html, 'html.parser')

# css선택자로 필요한 정보를 찾아냄
word = soup.select_one('.h3YV2d')

# 해당 요소 출력
print(word.text)
