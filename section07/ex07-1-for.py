'''
ex07-1-for.py

for문
    값의 범위나 횟수가 정해져 있을 때 사용
    while문보다 사용 빈도가 높다.

for 변수 in 반복가능한객치:
    반복실행문
'''

pwd = input("비밀번호를 입력하세요 >>")

ch_count = 0
num_count = 0

#in 뒤에 여러 개의 값을 가지는 변수(list, tuple, string, set 등)를 넣고
#그 값을 하나하나씩 인덱스 번호 대로 for 뒤에 오는 변수(ch)에 넣어줌.
for ch in pwd: #abcd1234라고 썼을 때,
    # 1:ch=a,
    # 2:ch=b...
    # 5:ch=1
    # 6:ch=2...
    if ch.isalpha(): #문자 여부
        ch_count += 1
    elif ch.isnumeric(): #숫자 여부
        num_count += 1
if ch_count > 0 and num_count >0:
    print("가능한 비밀번호입니다.")
else:
    print("불가능한 비밀번호입니다.")