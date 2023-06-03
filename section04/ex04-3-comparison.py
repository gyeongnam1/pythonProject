'''
ex04-3-comparison.py

관계 연산자
    2개 항을 비교하여 그 결과를 논리(bool) 자료형으로 반환
    ex) >, >=, < <=, ==, !=
'''
a = 15
print('{} > 10 : {}'.format(a, a>10)) #a>10은 관계연산자이니까 결과값이 T, F로 {}에 들어감
print('{} < 10 : {}'.format(a, a<10))
print('{} >= 10 : {}'.format(a, a>=10))
print('{} <= 10 : {}'.format(a, a<=10))
print('{} == 10 : {}'.format(a, a==10))
print('{} != 10 : {}'.format(a, a!=10))
