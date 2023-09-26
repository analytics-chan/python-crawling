# 폴더 생성하기
import os

# 폴더가 있는지 확인 True/False로 출력됨
# print(os.path.exists('chapter6/지수'))

# 폴더가 있을 경우 생성하지 않음
if not os.path.exists('chapter6/지수'):
    os.mkdir('chapter6/지수')

# 폴더 생성
# os.mkdir('chapter6/지수')
