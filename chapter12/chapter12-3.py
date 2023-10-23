# 토요코인 크롤링 3단계
import requests
from bs4 import BeautifulSoup

url = "https://www.toyoko-inn.com/korea/search"

data_obj = {
    'lcl_id': 'ko',
    'prcssng_dvsn': 'dtl',
    'sel_area_txt': '한국',
    'sel_htl_txt': '토요코인 서울강남',
    'chck_in': '2023/11/07',
    'inn_date': '1',
    'sel_area': '8',
    'sel_htl': '00282',
    'rsrv_num': '1',
    'sel_ldgngPpl': '1'
}

response = requests.post(url, data=data_obj)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
beds = soup.select('ul.btnLink03')
# print(beds)

for i, bed in enumerate(beds, 1):
    links = bed.select('a')
    if len(links) > 0:
        print('잔실 있음!')
        # if i <= 3:
        #     print('싱글 잔실 있음!')
        # elif i <= 5:
        #     print('더블 잔실 있음')