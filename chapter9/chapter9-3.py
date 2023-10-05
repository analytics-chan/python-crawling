# 데이터 전처리 테스트
# view = "조회수 1.5만회"
view = "조회수 3.4천회"

view = view.replace('조회수', '').replace('회', '').strip()

if "만" in view:
    view = float(view.replace('만', '')) * 10000
elif "천" in view:
    view = float(view.replace('천', '')) * 1000

print(view)

