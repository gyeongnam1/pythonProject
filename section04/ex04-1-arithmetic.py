'''
ex04-1-arithmetic.py

연산자
    특정한 작업을 수행하기 위해서 사용하는 기호

1. 산술 연산자
    숫자 계산을 할 때 사용하느 연산자.
    +, -, *, **(거듭제곱), /, //(나눴을 때 몫), %(나눴을 때 나머지)
'''

a=7
b=2
#덧셈
print('{} + {} = {}'.format(a, b, a+b))
print('계산한 값은 {}입니다'.format(a+b))

#뺄셈
print('{} - {} = {}'.format(a, b, a-b))

#곱셈
print('{} * {} = {}'.format(a, b, a*b))

#거듭제곱
print('{} ** {} = {}'.format(a, b, a**b))

#나누기
print('{} / {} = {}'.format(a, b, a/b))

#몫
print('{} // {} = {}'.format(a, b, a//b))

#나머지
print('{} % {} = {}'.format(a, b, a%b))




