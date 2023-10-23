# slack bot test
import requests

token = "xoxb-6080493949460-6071421399974-jrG5lJkj8Rmrp23v1ds5tIQA"
channel = "#crawling-practice-test"
text = "slack bot 테스트 중입니다."

requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": text})