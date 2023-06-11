'''
ex14-1-copyFile.py

파일 복사
    원본 읽기 -> 버퍼에 담기(memory에 저장) -> 복사본 파일에 쓰기

open 함수 모드
    b(binary mode) : 해당 파일의 데이터를 바이너리 파일로 인식하고 입출력.
'''

buffer_size = 1024 #1024 byte -> 1 kb
with open('../section13/hello.txt', 'rb') as source:
    with open('hello2.txt', 'wb') as copy:
        while True:
            buffer = source.read(buffer_size) #버퍼 사이즈만큼 읽음
            if not buffer:
                break
            copy.write(buffer)
print('hello2.txt 파일이 복사되었습니다.')
#인코딩을 안 해도 됨. binary이니까.