'''
ex02-9-mutable-immutable.py

mutable - 메모리 값을 변경할 수 있는 객체(값만 바뀌지 주소가 바뀌지 않음)
    리스트(list), 세트(set), 딕셔너리(dict)
'''
me = [1, 2, 3]
print(me)
print(id(me)) #주소값 프린트. 1945921342976
me.append(4)
print(me)
print(id(me)) #주소값 프린트. 1945921342976

'''
immutable - 메모리 값 변경 불가
    정수(int), 실수(float), 문자열(str), 튜플(tuple) (값을 바꾸면 주소값이 바뀜)
    *다른 변수가 같은 값을 가지게 되면(you = 10) 그 변수도 같은 주소값(140719961007176)을 참조
'''
me = 10
print(me)
print(id(me)) #140719961007176
me += 1 #me = me + 1
print(me)
print(id(me)) #140719961007208