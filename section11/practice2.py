'''
지역변수(local)
    함수 내부에서 선언. 내부에서만. 함수 종료시 없어짐
전역변수(global)
    함수 외부에서 선언. 내부 외부 모두.
'''

g = '전역'

def gandl():
    l = '지역'
    g = '전역1'
    print(g, '변수입니다')
    print(l, '변수입니다.')

def gandl2():
    l = '지역2'
    print(g, '변수입니다')
    print(l, '변수입니다.')

def gandl3():
    l = '지역'
    g = '변경된 전역이 아닌 새로운 지역'
    print(g, '변수입니다')
    print(l, '변수입니다.')

gandl()
gandl2()
gandl3()
print(g)

#전역변수를 수정하고 싶을 때
total = 0
def gift(dic, who, money):
    global total
    total += money
    dic[who] = money

wedding = {}
gift(wedding, '영희', 5)
gift(wedding, '철수', 20)
gift(wedding, '이모', 25)
print('축의금 명단 : {}'.format(wedding))
print('전체 축의금 : {}'.format(total))