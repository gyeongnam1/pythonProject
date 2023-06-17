'''
ex16-2-destructor.py

소멸자
    인스턴스가 소멸될 때 자동으로 호출된다.

소멸자 선언 방법
    __del()__
'''

class Service:
    def __init__(self, service):
        self.service = service
        print('{} Service가 시작되었습니다.'.format(self.service))

    def __del__(self):
        print('{} Service가 종료되었습니다.'.format(self.service))

#실행코드
s = Service('길 안내')
del s   #강제로 종료

s2 = Service('커피 주문')

print('프로그램 종료!')
#밑에 거 다 실행되다가 객체가 사라질 때 소멸됨.

