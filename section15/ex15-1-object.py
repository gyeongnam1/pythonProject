'''
ex15-1-object.py

클래스(class)
    객체를 생성하기 위한 템플릿.
    객체를 만드는 설계도.
    붕어빵 틀, 와플 기계
    객체화(인스턴스화) - 메모리에 올리는 것

객체(object)
    현실 세계에 존재하는 물리적, 추상적 개념을
    프로그램으로 표현한 것.
    예) 물리적 - 자동차, 컴퓨터, 모니터, 나무(?) 등등
        추상적 - 주문 정보, 배송 정보, 등등
        => 문서화할 수 있으면 객체.

객체 구성
    초기화용 - 생성자(객체가 만들어지기 전)
    속성 - 변수로 표현.(자동차에는 모델명, cc, 브랜드, 가격 등)
    기능 - 메소드(method. 함수)로 표현.(자동차는 드라이브)

가비지 컬렉터(Garbage Collector)
    메모리 관리를 자동으로 처리하여 사용하지 않는 객체를 식별하고 제거
'''

class Computer: #클래스에 종속된 함수를 method라고 하는 것
    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print('CPU = {}'.format(self.cpu))
        print('RAM = {}'.format(self.ram))
        print('VGA = {}'.format(self.vga))
        print('SSD = {}'.format(self.ssd))
#여기까지는 class 정의

desktop = Computer() #Computer 객체 생성
desktop.set_spec('i7','16GB','GTX3060','512GB')
desktop.hardware_info()
print()
desktop.cpu ='i9'
desktop.hardware_info()
print()

macbook = Computer()
macbook.set_spec('m2','16GB','M2','512GB')
macbook.hardware_info()