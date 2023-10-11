# 데이터 수집하기
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/field_submit.naver?menu=market_sum&returnUrl=http://finance.naver.com/sise/sise_market_sum.naver&fieldIds=quant&fieldIds=per&fieldIds=roe&fieldIds=pbr&fieldIds=reserve_ratio"

# "https://finance.naver.com/sise/field_submit.naver?menu=market_sum&returnUrl=http://finance.naver.com/sise/sise_market_sum.naver&fieldIds=quant&fieldIds=per&fieldIds=roe&fieldIds=pbr&fieldIds=reserve_ratio"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

trs = soup.select("table.type_2 > tbody > tr[onmouseover='mouseOver(this)']")

for tr in trs:
    # nth-child 사용 방법
    name = tr.select_one('td:nth-child(2)').text
    per = tr.select_one('td:nth-child(7)').text
    roe = tr.select_one('td:nth-child(8)').text
    pbr = tr.select_one('td:nth-child(9)').text
    reserve_ratio = tr.select_one('td:nth-child(10)').text
    print(name, per, roe, pbr, reserve_ratio)