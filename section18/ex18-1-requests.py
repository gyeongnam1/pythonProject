'''
ex18-1-requests.py

requests 라이브러리
    HTTP 요청을 보내기 위한 간편하고 인기있는 라이브러리
    이를 사용하여 웹페이지 데이터를 가져오거나, API와 상호작용할 수 있다.

라이브러리 설치 방법
pip install requests

#라이브러리 설치 에러 발생시
pip install chardet
pip install brotli
'''

import requests

url = 'https://entertain.naver.com/ranking/read'
param = {               #param => parameter. url에 보면 ? 전까지가 경로 같은 거고 그 뒤가 매개변수 같은 것
        'oid':'311',
        'aid':'0001581475'
}
response = requests.get(url, params=param)
print(response.text)