import requests
from bs4 import BeautifulSoup

response = requests.get('https://play.google.com/store/apps/details?id=com.starbucks.co&hl=ko-KR')

html = response.text

soup = BeautifulSoup(html, 'html.parser')

lists = soup.select('.AJTPZc')

# print(lists)

for l in lists:
  t = l.text
  print('1' + t)