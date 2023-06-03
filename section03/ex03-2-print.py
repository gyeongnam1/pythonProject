'''
ex03-2-print.py
print() 함수 사용법
    sep : 출력할 value의 구분 문자
    end : value 출력 후 출력할 문자(기본값 '\n')
    file : 출력 방향 지정
'''

print('재미있는', "파이썬") #기본적으로 띄어쓰기
print('python', "java", 'C', sep=',') #띄어쓰기 대신에 다른 걸로 구분

print('안녕', end='') #다른 프린트 함수를 하면 원래 개행이 기본(원래 end = '\n'인 것을 없애줌).
print('하세요')

fos = open("sample.py", mode='wt') #file output stream
    #메모장 같이 파일 하나 열고, wt라 함은 여기에 text를 write하겠다는 뜻.
    #그러고 이 파일은 fos에 넣음
print('print("Hello World")', file=fos)
    #이 열어놓은 파일인 fos에 print("Hello World")를 적겠다.
fos.close() #파일 닫기