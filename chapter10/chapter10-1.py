# 데이터 수집하기
import requests
from bs4 import BeautifulSoup

# HTTP 302 방식
url = "https://finance.naver.com/sise/field_submit.naver?menu=market_sum&returnUrl=http://finance.naver.com/sise/sise_market_sum.naver&fieldIds=quant&fieldIds=per&fieldIds=roe&fieldIds=pbr&fieldIds=reserve_ratio"

# "https://finance.naver.com/sise/field_submit.naver?menu=market_sum&returnUrl=http://finance.naver.com/sise/sise_market_sum.naver&fieldIds=quant&fieldIds=per&fieldIds=roe&fieldIds=pbr&fieldIds=reserve_ratio"

# 페이지 처리
# "https://finance.naver.com/sise/field_submit.naver?menu=market_sum&returnUrl=http://finance.naver.com/sise/sise_market_sum.naver?&page=2&fieldIds=quant&fieldIds=per&fieldIds=roe&fieldIds=pbr&fieldIds=reserve_ratio"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

trs = soup.select("table.type_2 > tbody > tr[onmouseover='mouseOver(this)']")

for tr in trs:
    # nth-child 사용 방법
    name = tr.select_one('td:nth-child(2)').text
    per = tr.select_one('td:nth-child(8)').text
    roe = tr.select_one('td:nth-child(9)').text
    pbr = tr.select_one('td:nth-child(10)').text
    reserve_ratio = tr.select_one('td:nth-child(11)').text

    # 데이터 전처리 => N/A 값이 아닐 경우에만
    if per != 'N/A' and roe != 'N/A' and pbr != 'N/A' and reserve_ratio != 'N/A':
        per = float(per.replace(',', ''))
        roe = float(roe.replace(',', ''))
        pbr = float(pbr.replace(',', ''))
        reserve_ratio = float(reserve_ratio.replace(',', ''))
        print(name, per, roe, pbr, reserve_ratio)

     
    # print(name, per, roe, pbr, reserve_ratio)