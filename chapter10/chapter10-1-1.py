import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.naver"

# URL Encode
# "https://finance.naver.com/sise/field_submit.naver?menu=market_sum&returnUrl=http%3A%2F%2Ffinance.naver.com%2Fsise%2Fsise_market_sum.naver&fieldIds=quant&fieldIds=per&fieldIds=roe&fieldIds=pbr&fieldIds=reserve_ratio"

# URL Decode
# "https://finance.naver.com/sise/field_submit.naver?menu=market_sum&returnUrl=http://finance.naver.com/sise/sise_market_sum.naver&fieldIds=quant&fieldIds=per&fieldIds=roe&fieldIds=pbr&fieldIds=reserve_ratio"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# print(soup)

tables = soup.select('#contentarea > div.box_type_l > table.type_2 > tbody > tr')
# print(tables)

#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2)
#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(3)

# title

for table in tables:
    # title = table.select_one('a.tltle')

    # if title == None:
    #     pass
    # else:
    #     title.text

    try:
        title = table.select_one('a.tltle').text
        # print(title)
    except:
        pass

    print(title)