'''
ex14-2-csvReader.py

CSV(comma-seperated values)
    필드를 쉼표(,)로 구분한 텍스트 데이터 파일.
'''

student_list = []
with open('학생명단 .csv', 'rt', encoding="UTF-8") as file:
    file.readline() #첫째줄 날리기(학번,이름,주소,연락처)
    while True:
        line = file.readline() #다음줄부터 line에 넣기.
        if not line:
            break

        student = line.split(',') #line에 넣은 것을 쉼표 단위로 잘라서 리스트로 입력
        student_list.append(student) #student_list에 첨가
print(student_list)