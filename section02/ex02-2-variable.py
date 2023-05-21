'''
ex02-2-variable.py

변수(variable)
    어떤 데이터를 저장하고자 할 때 사용하는 메모리 저장 공간.
    저장공간의 이름을 붙여준 것을 변수라한다.

변수명 = 값

변수명 규칙
    영문, 한글, 숫자, 밑줄(_)로 구성된다.
    특수문자(!@#$%^&*()_+ 등) 사용할 수 없다.
    대문자와 소문자를 구분한다.
    변수명의 첫 글자를 숫자로 사용할 수 없다.
    키워드(list, dict, if, for, and 등)은 사용할 수 없다.

'''
name = 'Alice'
character = "Mimi" #큰따옴표도 오케이
print(name)
print(character)
age = 25
print(age)
address = '''우편번호 123456 
서울시 서대문구 신촌 123-45
'''
# 개행까지 그대로 알아서 프린트 해줌!

print(address)

'''
잘못된 변수명 예시
'''
# 2mybar = 'Python1' #숫자로 시작
# my-var = 'python2' #특수 문자
# my var = 'python3' #공백

'''
여러 값 할당
'''
x, y, z = '피카츄', '라이츄', '파이리'
print(x)
print(y)
print(z)
print(x,y,z) # 이건 내가 해봄

'''
여러 변수에 대한 하나의 값
'''
x = y = z = '꼬부기'
print(x)
print(y)
print(z)
