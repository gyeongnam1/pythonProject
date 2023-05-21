'''
ex02-4-string.py

문자열(String)
    하나 이상 연속된 문자(character) 들의 나열.
    파이썬에서는 문자열 자료형은 큰따옴표(" ")
    또는 작은따옴표(' ') 사이에 위치
'''

#'hello'와 "hello" 동일
print("hello" == 'hello') #값이 같으면 True 반환

'''
변수에 문자열 할당
'''
str = "hello"
print(str)

'''
여러 줄 문자열
    세 개의 따옴표를 사용하여 변수에 여러 줄 문자열을 할당
'''

str=''' 피카츄, 라이츄, 파이리, 꼬부기
버터플, 야도란, 피존튜, 또가스
'''
print(str)

'''
문자 배열=> 문자열
    문자열 인덱싱(indexing)
    h   e   l    l    o     <==  문자열
    0   1   2   3   4     <== 인덱스
   -5  -4 -3  -2  -1    <== 마이너스 인덱스
'''
str = 'hello'
print(str[1]) #한글자 한글자 접근이 가능
print(str[-4]) #파이썬은 마이너스 인덱싱도 같이 있음
print(str[1] == str[-4])

'''
문자열 슬라이싱
    슬라이스 구문을 사용하여 문자를 반환할 수 있다.
    문자열의 일부를 반환하려면 시작 인덱스와 끝 인덱스를 콜론으로 구분
'''
str = "Hello, World"
print(str[2:5]) #5 앞에까지. 5는 포함이 안됨/ 2는 포함
#처음부터 인덱스 번호 앞까지 슬라이스
print(str[:5]) #str[0:5]과 같음
#인덱스 번호부터 끝까지 슬라이스
print(str[2:])

str = "Hello, World"
#대문자로 바꾸기
print(str.upper())
#소문자로 바꾸기
print(str.lower())

#문자열 바꾸기
str = "Hello, World"
print(str.replace("H", "J"))