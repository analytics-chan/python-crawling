import openpyxl

keyword = input('파일을 붙여넣기 해주세요 >>> ')

print('파일명 >>> ', keyword)

# wb = openpyxl.load_workbook(rf"{keyword}")
wb = openpyxl.load_workbook(keyword)
sheet = wb.get_sheet_by_name('Sheet1')
# a = sheet['A1'].value

# print(a)

key_box = []

for i in range(1, 100):
    val = sheet[f'A{i}'].value

    if val != None:
        key_box.append(val)
    else:
        break

print(key_box)