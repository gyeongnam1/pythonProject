'''
ex07-4-for-dict2.py
'''

students = [
    {'이름':'John', '국어':90, "영어":80, "수학":92},
    {'이름':'Emily', '국어':49, "영어":67, "수학":88},
    {'이름':'Michael', '국어':100, "영어":89, "수학":58},
    {'이름':'Sandra', '국어':99, "영어":98, "수학":100}
]

#테이블 헤더 출력
print("이름 \t국어\t영어\t수학")
print("=============================")

#각 학생 성적 출력
for student in students:
    name = student["이름"]
    korean = student["국어"]
    english = student["영어"]
    math = student["수학"]
    print(f"{name}\t{korean}\t{english}\t{math}")
