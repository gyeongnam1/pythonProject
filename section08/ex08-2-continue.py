'''
ex08-2-continue.py

continue
    while 문이나 for 문과 같은 반복문을 강제로 건너뛰게 한다.
'''
total = 0
for a in range(1,101):
    if a % 3 == 0: #3의 배수
        continue #아래 코드는 실행되지 않고 skip
    total += a
    print('a: {}, total: {}'.format(a, total))

print(total)