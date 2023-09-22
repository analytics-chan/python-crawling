import requests
from bs4 import BeautifulSoup
import time
import pyautogui

# keyword = input('검색어를 입력하세요 >>> ')
# page_num = int(input('몇 페이지까지 추출하시겠습니까? >>> '))

# response = requests.get(f'https://www.coupang.com/np/search?component=&q={keyword}&channel=user&page={page_num}')
# response = requests.get(f'https://www.coupang.com/np/search?component=&q=게이밍+마우스&channel=user')
response = requests.get(f'https://www.coupang.com/np/search?component=&q=%EA%B2%8C%EC%9D%B4%EB%B0%8D+%EB%A7%88%EC%9A%B0%EC%8A%A4&channel=user')
html = response.text
soup = BeautifulSoup(html, 'html.parser')

print(html)
# print(soup.select_one('.hit-count').text)

# articles = soup.select('#productList')
# links = soup.select_one('.search-product-link').attrs['href']
# print("links")

# for a in articles:
#     links = a.select('.search-product-link')
#     print(links)

    # response = requests.get(links)
    # html = response.text
    # soup = BeautifulSoup(html, 'html.parser')

    # title = soup.select_one('h2.prod-buy-header__title')
    # print(title)
    # time.sleep(0.3)

# for i in range(1, page_num, 1):
#     response = requests.get(f'https://www.coupang.com/np/search?component=&q={keyword}&channel=user&page={page_num}')
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')

#     articles = soup.select('#productList')

#     for a in articles:
#         links = a.select('.search-product-link')

#         response = requests.get(links)
#         html = response.text
#         soup = BeautifulSoup(html, 'html.parser')

#         title = soup.select_one('h2.prod-buy-header__title')
#         print(title)
#         time.sleep(0.3)

# soup.select_one('.search-product-wrap-img').attrs['src']

# print(soup)

print('hello world')

    # for i in range(1, page_num, 1):
    #     response = requests.get(f'https://www.coupang.com/np/search?component=&q={keyword}&channel=user&page={page_num}')
    #     # response = requests.get(f'https://www.coupang.com/np/search?component=&q=게이밍+마우스&channel=user')
    #     html = response.text
    #     soup = BeautifulSoup(html, 'html.parser')

    #     articles = soup.select('#productList')

    #     print(articles)

    # for a in articles:
    #     test = a.select('.search-product')
    #     print(test)
        # links = a.select('.search-product-link')
