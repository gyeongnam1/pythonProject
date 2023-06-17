'''
함수(function)
    하나의 특별한 목적의 작업을 수행하기 위해
    독립적으로 설계된 프로그램 코드의 집합

def 함수이름(매개변수):
    코드 실행문
    return 반환값
'''

# welcome 함수 정의 (실행X)
def welcome():
    print('hello python')
    print('Nice to meet you')
# 매개변수 X, 리턴 X -> 실행하고 끝나는 함수

welcome() #함수 호출(실행)

def add(a, b):
    print(a+b)

add(3,5)
def introduce(name, age):
    print('내 이름은 {}이고 나이는 {}입니다.'.format(name, age))

introduce('홍길동', 25)

def address():
    str = '우편번호 1234\n'
    str += '서울시 마포구 염리동'
    return str

result = address()
print(result)

def plus(num1, num2):
    return num1 + num2

result = plus(5,7)
print(result) # 왜 바로 print(plus(5,7))을 안 하는지?... 아 된다고 하심.




