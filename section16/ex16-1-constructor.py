'''
ex16-1-constructor.py

생성자
    객체를 생성할 때 생성자가 자동으로 호출된다
    주로 객체 초기화용으로 사용.

생성자 선언 방법
    __init()__
'''
class USB:
    def __init__(self, capacity): #생성자
        self.capacity = capacity #생성 전에 뭔가 해야 하면 여기 밑에다 해야 함.

    def info(self):
        print('{}GB USB'.format(self.capacity))

#실행
usb = USB(128) #아예 생성을 할 때 값을 넣어줘야 함.
usb.info()

usb2 = USB(1024)
usb2.info()