'''
ex09-4-etc.py
'''

# len() 데이터 길이. text나 list 등 어쨌든 값이 여러 개인 경우
text = "good night"
print(len(text))

#abs() 절대값
result = abs(-10)
print(result)

# format() 문자 포맷 관련 함수
result = format(100000) #str(100000)와 같다
result = format(100000, ',') #천 단위 표시 해줌.
print(result)

#max() 최대값 반환
result = max(1, 10)
print(result)
li = [5,3,1,2,7,9,-100]
result = max(li)
print(result)

#min() 최소값 반환
result = min(li)
print(result)

#pow() 거듭제곱
result = pow(10,2)
print(result)

#sorted() 정렬
my_li = [5,3,7,14,1,2]
result = sorted(my_li)
print(result)

#역정렬
result = sorted(my_li, reverse=True)
print(result)

#zip() 같은 인덱스 번호끼리 튜플로 묶어줌
names = ['james', 'emily', 'amanda']
scores = [60, 70, 80]
for student in zip(names, scores):
    print(student)

for name, score in zip(names, scores):
    print("{}의 점수는 {}입니다.".format(name, score))