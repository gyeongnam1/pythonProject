'''
ex17-5-exception5.py

예외를 강제로 발생시키기!
'''

try:
    raise Exception('강제로 발생시킨 예외')
except Exception as e:
    print('발생한 예외 메시지는 다음과 같습니다.')
    print(e)
