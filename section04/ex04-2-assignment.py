'''
ex04-2-assignment.py

대입 연산자
    변수에 값을 저장하기 위해 사용하는 연산자

print 형식 문자
%d : 숫자 데이터
%f : 실수 데이터
%o : 8진수 데이터
%x : 16진수 데이터
%s : 문자열 데이터
%c : 문자 하나 데이터
'''

a, b = 10, 20
print('a = %d, b=%d ' % (a, b))
print('a = {}, b={} '.format(a,b)) #똑같음.

#두 변수의 값을 바꾸려면(switch) 원래 다른 언어는 임시 변수(temp)가 필요
#근데 파이썬에서는......
a, b = b, a
print('a = %d, b = %d ' %(a,b))

'''
복합 대입 연산자
    +=
        ex) x += 3  ->   x = x+3
    -+
        ex) x -= 3  ->   x = x-3
'''
piggy_bank = 0
money = 10000
piggy_bank += money #piggy_bank = piggy_bank + money
print("저금통에 용돈 {}원을 넣었습니다.".format(money))
print("지금 저금통에는 {}원이 있습니다.".format(piggy_bank))

snack = 2000
piggy_bank -= snack #piggy_bank = piggy_bank - snack
print('저금통에서 스낵 구입비 {}원을 뺐습니다.'.format(snack))
print("지금 저금통에는 {}원이 있습니다.".format(piggy_bank))

