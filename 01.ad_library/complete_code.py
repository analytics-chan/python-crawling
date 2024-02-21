import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from tkinter import Tk, filedialog
import openpyxl
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import requests
import random
import hashlib
from tkinter import messagebox
import re
import os
import unicodedata
import subprocess 
import chromedriver_autoinstaller

def open_folder_on_top(path):
    normalized_path = os.path.normpath(path)
    if os.path.isdir(normalized_path):
        subprocess.Popen(f'explorer "{normalized_path}"', shell=True)
    else:
        print(f"지정된 경로가 폴더가 아닙니다: {normalized_path}")

def remove_illegal_chars(filename):
    illegal_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in illegal_chars:
        filename = filename.replace(char, '')
    return filename

def clean_text(text):
    text = text.strip()
    return text

def restore_string(text):
    return unicodedata.normalize('NFC', text)

def clean_filename(filename):
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)
    return filename

def download_image(url, save_path):
    try:
        urllib.request.urlretrieve(url, save_path)
        print(f"이미지 저장 성공: {save_path}")
        return True
    except Exception as e:
        print(f"이미지 저장 실패: {save_path}")
        print("에러:", e)
        return False

def login_facebook(driver):
    login_url = "https://www.facebook.com/login"
    driver.get(login_url)
    time.sleep(2)
    print('\n페이스북 로그인 및 인증을 마치신 후 엔터키를 입력하세요.\n')
    input()
    time.sleep(3)

def extract_info(driver, keyword, save_path):
    keyword_folder = os.path.join(save_path, keyword)
    if not os.path.exists(keyword_folder):
        os.makedirs(keyword_folder)

    url = f"https://business.facebook.com/ads/library/?active_status=active&ad_type=all&country=KR&q={keyword}&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all&content_languages[0]=ko"
    driver.get(url)
    time.sleep(5)

    def scroll_down(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    scroll_down(driver)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "광고 정보"
    ws.append(['광고 번호', '시작일', '라이브러리 ID', '광고주명', '본문'])

    # 광고 게시 시작 날짜만 포함하는 span 요소를 찾기 위한 함수 정의
    def find_date_span(tag):
        return (tag.name == "span" and
                re.search("게재 시작함", tag.text) is not None)

    ads = soup.select('div.x1dr75xp.xh8yej3.x16md763 > div.xrvj5dj.xdq2opy.xexx8yu.xbxaen2.x18d9i69.xbbxn1n.x143o31f.x7sq92a.x1crum5w > div')
    for i, ad in enumerate(ads, start=1):
        try:
            images = ad.find_all('img')[1:]
            date_element = ad.find(find_date_span)  # 수정된 부분
            product_id_element = ad.select_one('.xt0e3qv')
            advertiser_name_element = ad.select_one('.x8t9es0.x1fvot60.xxio538.x108nfp6.xq9mrsl.x1h4wwuj.x117nqv4.xeuugli')
            body_element = ad.select_one('._4ik4._4ik5[style*="line-height"]')

            # 예외 처리를 추가하여 각 요소가 존재하지 않는 경우에도 처리할 수 있도록 합니다.
            startday_text = date_element.get_text(strip=True) if date_element else '시작일을 찾을 수 없습니다.'
            product_id = product_id_element.get_text(strip=True) if product_id_element else '상품 id를 찾을 수 없습니다.'
            advertiser_name = advertiser_name_element.get_text(strip=True) if advertiser_name_element else '광고주명을 찾을 수 없습니다.'
            body_text = body_element.get_text(strip=True) if body_element else '본문에 기재된 내용을 찾을 수 없습니다.'
            
            clean_body_text = clean_text(body_text.replace('\u2028', ' '))
            advertiser_name = restore_string(clean_filename(advertiser_name))
            ws.append([i, remove_illegal_chars(startday_text), remove_illegal_chars(product_id), remove_illegal_chars(advertiser_name), remove_illegal_chars(clean_body_text)])
            
        except openpyxl.utils.exceptions.IllegalCharacterError:
            print(f"오류: 광고 번호 {i}에 처리할 수 없는 문자가 포함되어 있어 워크시트에 추가하지 못했습니다.")
            ws.append([i, "데이터를 처리할 수 없습니다."])

        for j, img in enumerate(images):
            img_url = img.get('src')
            if img_url:
                img_save_path = f"{keyword_folder}/{i}_{j}_{advertiser_name}.jpg"
                download_image(img_url, img_save_path)

    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    excel_save_path = f"{keyword_folder}/{keyword}_Meta광고라이브러리_{now}.xlsx"
    wb.save(excel_save_path)
    print(f"'{keyword}' 키워드 추출 완료")

if __name__ == "__main__":
    Tk().withdraw()

    continue_extraction = True

    while continue_extraction:
        keywords_input = input("검색할 키워드를 쉼표(,)로 구분하여 입력하세요: ")
        keywords = [keyword.strip() for keyword in keywords_input.split(',') if keyword.strip()]

        if not keywords:
            print("키워드가 입력되지 않았습니다. 프로그램을 종료합니다.")
            break
        else:
            save_path = filedialog.askdirectory(title="저장할 폴더를 선택하세요")
            if not save_path:
                print("폴더 선택이 취소되었습니다. 프로그램을 종료합니다.")
                break
            else:
                login_required = messagebox.askyesno("로그인 확인", "페이스북 로그인이 필요합니까?")

                chrome_service = ChromeService(executable_path=chromedriver_autoinstaller.install())
                chrome_options = Options()
                driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

                if login_required:
                    login_facebook(driver)

                for keyword in keywords:
                    try:
                        extract_info(driver, keyword, save_path)
                    except Exception as e:
                        print(f"\n{keyword} 키워드 추출 중 오류가 발생하였습니다. 에러 메시지: {e}\n")
                        continue

                open_folder_on_top(save_path)
                continue_extraction = messagebox.askyesno("추출 완료", "다른 키워드로 계속 추출하시겠습니까?")
                driver.quit()