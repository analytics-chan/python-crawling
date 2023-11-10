# slack bot test
# import requests

# 개인 계정 테스트
# token = "xoxb-6080493949460-6071421399974-jrG5lJkj8Rmrp23v1ds5tIQA"
# channel = "#crawling-practice-test"
# text = "slack bot 테스트 중입니다."

# requests.post("https://slack.com/api/chat.postMessage",
#     headers={"Authorization": "Bearer "+token},
#     data={"channel": channel,"text": text})

import requests

# ga4.sychoi@gmail.com 계정 테스트
# token = "xoxb-6162516044822-6154651620951-L2o9NGTkJtV8toLqgbNNzt6T"
token = 'xoxb-6162516044822-6154651620951-6Dq1Ua15rwfdKMaYgIzXJsGj'
channel = "#create-error-test-bot"
text = "슬랙 bot 테스트"

requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": text})