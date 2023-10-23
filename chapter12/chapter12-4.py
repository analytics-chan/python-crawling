# 토요코인 크롤링 4단계
import requests
from bs4 import BeautifulSoup
import time

token = "xoxb-6080493949460-6071421399974-jrG5lJkj8Rmrp23v1ds5tIQA"
channel = "#crawling-practice-test"
# text = "slack bot 테스트 중입니다."

def post_message(token, channel, text):
    requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+ token},
    data={"channel": channel,"text": text})

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

cnt = 1
while True:
    try:
        response = requests.post(url, data=data_obj)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        beds = soup.select('ul.btnLink03')
        # print(beds)

        for i, bed in enumerate(beds, 1):
            links = bed.select('a')
            if len(links) > 0:
                post_message(token, channel, "잔실 있음!")
                # print('잔실 있음!')
                # if i <= 3:
                #     print('싱글 잔실 있음!')
                # elif i <= 5:
                #     print('더블 잔실 있음')
    except:
        print('오류 발생했지만 계속 실행하겠습니다.')

    print(f'{cnt}번째 시도입니다.')
    time.sleep(10)
    cnt += 1