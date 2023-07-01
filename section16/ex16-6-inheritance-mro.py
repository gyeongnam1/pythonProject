'''
ex16-6-inheritance-mro.py
'''

class A:
    def greeting(self):
        print('안녕하세요, A입니다.')

class B(A):
    def greeting(self):     #오버라이딩 - 부모 클래스의 메서드를 재정의함
        print('안녕하세요, B입니다.')

class C(A):
    def greeting(self):     #오버라이딩 - 부모 클래스의 메서드를 재정의함
        print('안녕하세요, C입니다.')

class D(B,C):
    pass    #내부동작 필요 없고 빈껍데기만 필요할 때 pass 사용.
#본문은 없고 B와 C를 합치는 역할만 함.

#죽음의 다이아몬드
#실행 코드
x = D()
x.greeting()
#다중 상속이고 메서드가 같을 경우, 어느 게 호출될지 모름.

print(D.mro()) #mro() - 다중 상속 시 메서드 호출 순서를 알려줌