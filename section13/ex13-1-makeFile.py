'''
ex13-1-makeFile.py

파일 입출력(I/O - input/output)
    입력(input) 기존 파일 읽어들이는 것
    출력(output) 파일 생성, 내용 추가를 말한다.

open() 함수
    파이썬에서 open() 함수를 사용하여 파일을 열고 파일 객체 생성,
    이를 통해 파일을 읽고 쓸 수 있다.
'''

'''
file = open('myFile.txt', 'wt')
print('myFile.txt 파일이 생성되었습니다.')
file.close() #메모리에서 사라진다. open을 했으면 꼭 해줘야 메모리가 터지지 않음.
'''

# with 문 - 자동으로 close()를 해준다.
with open('myFile.txt', 'wt') as file:
    print('myFile.txt 파일이 생성되었습니다.')
