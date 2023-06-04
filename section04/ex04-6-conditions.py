'''
ex04-6-conditions.py

조건 연산자(삼항 연산자)
    조건식 결과에 따라 참 또는 거짓의 결과를 반환한다.
    참 if 조건식 else 거짓
'''

a = 20
b = 100
result = (a-b) if (a >= b) else (b-a) #if문도 있긴 한데 한 줄로 간단하게 생성 가능
# result = if (a >= b) (a-b) else (b-a) #if조건을 먼저 쓰면 안 되네. 순서가 정해져 있음.
print('{}과 {}의 차이는 {}입니다.'.format(a, b, result))