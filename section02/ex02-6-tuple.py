'''
ex02-6-tuple.py

튜플
    단일 변수에 여러 항목을 저장하는 데 사용된다.
    순서가 있고, 변경할 수 없는 list
    둥근 괄호로 작성된다.

'''

thistuple = ('피카츄', '라이츄', '파이리')
print(thistuple)

#튜플의 길이
print(len(thistuple))

#항목 접근
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])

#튜플 값 변경 방법
thistuple = ('피카츄', '라이츄', '파이리')
thiscast = list(thistuple) #list로 casting(형변환). ['피카츄', '라이츄', '파이리'],
thiscast[1] = '잠만보' # ['피카츄', '잠만보', '파이리']
thistuple = tuple(thiscast) #다시 튜플로 바꿔주는 것. ('피카츄', '잠만보', '파이리')
print(thistuple) #억까. 그냥 새로 계속 만드는 것뿐

#튜플 압축 풀기
thistuple = ('피카츄', '라이츄', '파이리', '꼬부기')
(p1,p2,p3,p4) = thistuple
print(p1)
print(p2) #ctrl + d = 줄복사 / ctrl + y = 줄삭제 / ctrl 누르고 커서 옆으로 이동하면 단어 단위로 이동
print(p3)
print(p4)

#두 개 튜플 조인
thistuple1 = ('피카츄', '라이츄', '파이리', '꼬부기')
thistuple2 = ('버터플', '야도란', '피존투', '또가스')
thistuple3 = thistuple1 + thistuple2
print(thistuple3)