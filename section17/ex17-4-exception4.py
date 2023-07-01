'''
ex17-4-exception4.py

try:
    정상코드 영역
except:
    예외 발생시 처리 영역
else:
    예외가 발생하지 않으면 처리되는 영역(try 영역의 후처리에 씀. 거의 안 쓰기도...)
finally:
    항상 실행되는 영역(정상이든 예외이든 실행되어야 하는 코드)
'''
try:
    print('서버에 접속합니다.')
    a = int(input('제수를 입력하세요 >>>'))
    b = int(input('피제수를 입력하세요 >>> '))

    result = a/b
except:
    print('예외가 발생했습니다.')
else:
    print('{} / {} = {}'.format(a, b, result))
finally:
    print('서버 접속을 종료합니다.') #서버가 터지는 걸 막기 위해. 통신 끊겼다는 걸 알려줘야 함.