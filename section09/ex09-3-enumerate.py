'''
ex09-3-enumerate.py

enumerate() 함수
    list, tuple, string 등 자료형을 입력받으면
    인덱스 값을 포함하는 enumerate 객체를 돌려준다.
'''
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for month, day in enumerate(months): #month는 인덱스값, day는 value
    print('{}월 = {}일'.format(month+1, day))