'''
ex18-5-getRankPage.py
'''
import requests
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/chart'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
music_list = soup.find_all('p', class_='title')
artist_list = soup.find_all('p', class_='artist')

for idx, title in enumerate(music_list):
    print(idx+1, end='   ')
    print(title.text.strip(), end=' - ')
    print(artist_list[idx].find_all('a')[0].text.strip())
    #find_all을 한 이유는 p 테그 안에 a 테그가 2개인 경우에 앞에 0번째 a태그만 출력하겠다는 뜻.

