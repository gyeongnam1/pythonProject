'''
ex18-7-selenium-googleImages.py

selenium 패키지
    어플리케이션 테스트하기 위한 프레임웍.
    웹어플리케이션 다양한 브라우저 동작 테스트용
    웹 크롤링으로 많이 사용된다.
    java, python, c#, ruby 등 다양한 언어 지원
    ex) 브라우저 컨트롤

크롬 드라이버 설치 해야함
https://chromedriver.chromium.org/downloads

크롬 우측 상단 ... -> 도움말 -> 크롬 정보 -> 버전 확인 -> 같은 버전 chromedriver 다운로드

'''

import os
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service

import traceback

def download_image(keyword, num_images=10, output_dir='images'):
    #Chrome 드라아버 경로
    chrome_driver_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
#크롬 조작을 도와주는 애

    service = Service(executable_path=chrome_driver_path)
#서비스라는 객체에다가 경로 넣어줌

    #Chrome 드라이버 인스턴스 생성
    driver = webdriver.Chrome(service=service)
#드라이버라는 객체를 생성

    #Google 이미지 검색 페이지 접속
    driver.get('https://www.google.co.kr/imghp')

    #검색어 입력
    search_bar = driver.find_element(By.NAME, 'q')
#여기서 element는 html을 찾으라는 것. 서치바를 찾는 것. 'name'이라는 이름으로 태그된 것 찾기
    search_bar.send_keys(keyword) #키워드 입력
    search_bar.send_keys(Keys.RETURN) #엔터 입력. 키워드가 아니라 자판의 키 값 입력

    #페이지 로딩 대기
    time.sleep(2)

    #출력 디렉토리 생성
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
#디렉토리가 없으면 만들어줘

    #썸네일 요소 선택
    thumbnails = driver.find_elements(By.CSS_SELECTOR, '.rg_i')
#html 태그에서 복수의 요소를 가지고 옴.
# html, java script, css 중에서 css. 클래스가 '.', 즉 rg_i를 찾음

    #썸네일 클릭 및 이미지 다운로드
    for index, thumbnail in enumerate(thumbnails[:num_images]):
        try:
            thumbnail.click()
            time.sleep(2)

            #이미지 요소 대기 및 선택
            image = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".r48jcc.pT0Scc.iPVvYb")
                    #3개의 클래스 다 써줬음. 각각 앞에 .으로 연결. html에서는 띄어쓰기
                )
            )

            #이미지 URL 가져오기
            image_url = image.get_attribute('src')
        #이미지가 url이 원래 따로 있음. 이 경우 scr 옵션에 이미지 주소가 있음.

            if image_url.startswith('data:'):
                continue
        #주소로 되어 있는 이미지 외에 data로 되어 있는 이미지는 받지 않음

            headers = {"User-Agent":"Mozilla/5.0"}
            request = urllib.request.Request(image_url, headers=headers)
            with urllib.request.urlopen(request) as response:
                with open(f"{output_dir}/{keyword}_{index}.jpg", 'wb') as out_file:
                    out_file.write(response.read())

        except Exception as e:
            print(f"Error downloading image {index}: {e}")
            traceback.print_exc()

    #드라이버 종료
    driver.quit()

#실행 코드
keyword = "cute cat"
num_images = 10
output_dir = 'images'

#이미지 다운로드 함수 호출
download_image(keyword, num_images, output_dir)