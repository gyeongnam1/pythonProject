'''
ex14-5-csvReader2.py

모듈을 사용하지 않고 읽을 때.
=> 모듈을 썼을 때가 더 편하다.
'''

member_list =[]
with open('회원명단.csv', 'rt', encoding = 'UTF-8') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        member = line.split(',')
        member[0] = member[0].strip('"')
        member[2] =member[2].strip('\n')

        member_list.append(member)
print(member_list)