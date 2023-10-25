from datetime import datetime

today = datetime.today()
print(str(today)[:-7])

# import re

# test = '사용자 132명이 이 리뷰가 유용하다고 평가함'
# num = re.sub(r'[^0-9]', '', test)
# print(test, '\n', num)

# date = '2020년 3월 14일'

# if '년 ' and '월 ' and '일' in date:
#     date = date.replace('년 ', '-')
#     date = date.replace('월 ', '-')
#     date = date.replace('일', '')

# print(date)

# if date[5] == '-':
#     date.

# years = date.split('년')[0].strip()
# months = date.split('년')[1].split('월')[0].strip()
# days = date.split('년')[1].split('월')[1][:-1].strip()

# print(date.split('년'))

# print(date.split('년')[1].split('월'))

# print(date.split('년')[1].split('월')[1][:-1])

# print(years, months, days)

# print(len(months), len(days))

# if len(months) == 1:
#     months = '0' + months

# if len(days) ==1:
#     days = '0' + days

# print(f'{years}-{months}-{days}')