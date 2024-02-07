from datetime import datetime, timedelta

# 현재 날짜 및 시간 가져오기
now = datetime.now()

# 변수 초기화
a = "1-7"
b = "2-13"
c = "18시간전"
d = "2주전"

# 날짜 포맷 변경 함수
def convert_date_format(date_str):
    parts = date_str.split('-')
    month, day = map(int, parts)
    return now.replace(month=month, day=day).strftime("%Y-%m-%d")

# 결과 출력 함수
def print_result():
    print(f"a = \"{convert_date_format(a)}\"")
    print(f"b = \"{convert_date_format(b)}\"")

    if "시간전" in c:
        hours = int(c.split('시간전')[0])
        result_c = now - timedelta(hours=hours)
        print(f"c = {result_c.strftime('%Y-%m-%d ')}")

    if "주전" in d:
        weeks = int(d.split('주전')[0])
        result_d = now - timedelta(weeks=weeks)
        print(f"d = {result_d.strftime('%Y-%m-%d')}")

# 결과 출력
print_result()