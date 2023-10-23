# 토요코인 크롤링 1단계
import requests
from bs4 import BeautifulSoup

url = "https://www.toyoko-inn.com/korea/search/reserve/room"

# header = {'User-Agent' : 'Mozila/5.0'}

# response = requests.get(url, headers=header)
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
beds = soup.select('ul.btnLink03')
print(beds)