'''
ex02-7-set.py

set
    순서가 없다
    인덱싱되지 않는 컬렉션
    중복값 없다.
'''

thisset = {"피카츄", "라이츄", "파이리"} #실행할 때마다 순서 바뀜. 중복값 없음

print(thisset)

#항목 가져오기
for x in thisset: #thisset 길이만큼 반복
    print(x)

#값이 있는지 확인
thisset = {"피카츄", "잠만보", "야도란"}
print("피카츄" in thisset) #피카츄가 여기에 있느냐? 있으니 True로 출력됨
print("꼬부기" in thisset) #꼬부기가 여기 있느냐? 없으니 False로 출력됨

#항목 추가하기
thisset.add("꼬부기")
print(thisset)

#다른 Set 항목 추가
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"꼬부기", "잠만보", "뮤츠"}
thisset1.update(thisset2)
print(thisset1)

#항목 제거
thisset = {"피카츄", "라이츄", "파이리"}
thisset.remove("피카츄")
print(thisset)
#없는 항목 삭제 시 에러 발생.
#thisset.remove("피카츄")
#print(thisset)

thisset = {"피카츄", "라이츄", "파이리"}
thisset.discard("피카츄")
print(thisset)
#없는 항목 삭제 시 에러 발생 안함.
thisset.discard("피카츄")
print(thisset)

#항목 제거2
thisset.pop()
print(thisset) #원래 맨 뒤에 거 제거인데 순서가 없으므로 랜덤으로 하나씩 제거

#비우기
thisset.clear()
print(thisset)