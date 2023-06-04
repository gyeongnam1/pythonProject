'''
ex07-2-for-range.py

for 문과 range 함수

range()
    연속된 숫자를 만들어주는 함수
'''

dan = int(input('출력할 구구단을 입력하세요 >>>'))
'''
range(stop)
    0부터 stop 전까지 연속된 숫자를 만들어줌(0,1,2,...,(stop-1)).
'''
#0~9 range
for n in range(10): #매개변수(인자, 파라메타) 값 10
    print("{}×{}={} ".format(dan, n, dan*n), end='')
print()

'''
range(start, stop)
    시작 숫자부터 stop 전까지 연속된 숫자를 만들어줌
'''
#1~9 range
for n in range(1,10):
    print("{}×{}={} ".format(dan, n, dan*n), end='')
print()

'''
range(start, stop, step)
    step은 연속되는 숫자의 간격. 등차수열 같은??
'''
#1부터 2씩 증가 < 10
for n in range(1, 10, 2):
    print("{}×{}={} ".format(dan, n, dan * n), end='')
print()
