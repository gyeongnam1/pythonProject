'''
ex02-5-list.py

list
    단일 변수에 여러 항목을 저장하는 데에 사용된다.
    List 항목은 순서가 지정되고 변경 가능하며 중복값 허용
    List에는 다양항 데이터 유형이 포함될 수 있다.
    대괄호 사용
'''
thislist = ['피카츄', '라이츄', '꼬북이'] #각각 요소에 인덱스 번호가 있음
print(thislist)
print(thislist[0])

#list 길이
print(len(thislist)) #len() 함수로 리스트 길이를 알 수 있음.

#list 데이터 유형
list1 = ['피카츄', '라이츄', '파이리']
list2 = [1,2,3,4,5]
list3 = [True, False, True]
list4 = ['abc', 34, False, 40] #자료형을 섞어서도 가능

#항목 접근
thislist = ['피카츄', '라이츄', '파이리']
print(thislist[1])

#항목 변경
thislist[1] = '잠만보'
print(thislist)

#항목 변경 2개
thislist = ['피카츄', '라이츄', '파이리', '꼬부기', '버터플', '야도란']
thislist[1:3] = ['울먹이', '메타몽']
print(thislist)

#두 번째 세 번째 값을 하나의 값으로 변경
thislist = ['피카츄', '라이츄', '파이리', '꼬부기', '버터플', '야도란']
thislist[1:3] = ['잠만보']
print(thislist)

#항목 추가
thislist = ["피카츄", "라이츄", "파이리"]
thislist.append("꼬북이") #append 는 끝에 붙이기. 변수명.append("추가요쇼")
print(thislist)

#항목 추가 - 인덱스 번호로 추가
thislist = ["피카츄", "라이츄", "파이리"]
thislist.insert(1, '잠만보') #insert 는 중간에 넣기. 변수명.insert(넣을자리, "추가요소")
print(thislist)

#항목 값으로 제거
thislist = ["피카츄", "라이츄", "파이리"]
thislist.remove('라이츄')
print(thislist)

#항목을 지정된 인덱스로 제거
thislist = ["피카츄", "라이츄", "파이리"]
thislist.pop(2)  # thislist.remove(thislist[2]) 이것도 되네
print(thislist)

#마지막 값 제거
thislist = ["꼬부기", "버터플", "야도란", "피존투"]
thislist.pop() #인덱스 안 넣으면 마지막 거만 삭제
print(thislist)

#목록 삭제
thislist = ["피카츄", "라이츄", "파이리"]
thislist.clear() #변수 thislist가 사라진 게 아니라 그 안의 값만 사라진 것
print(thislist)

#확장
thislist = ["피카츄", "라이츄", "파이리"]
thislist.extend(['버터플', '잠만보'])
print(thislist)

#객체 자체 삭제
# del thislist
# print(thislist) #에러. 메모리에 thislist가 사라진 것.