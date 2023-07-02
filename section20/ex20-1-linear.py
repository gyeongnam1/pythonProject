'''
ex20-1-linear.py

자료구조
    데이터를 저장하고 조직화하는 방법론
    여러 개의 데이터를 어떻게 효율적으로 저장하고 삭제하는가

선형 리스트(LinearList)
    간단한 자료구조 중 하나로, 데이터를 일렬로 나여한 것.
'''

class LinearList():
    def __init__(self):
        self.linear = []     #빈 리스트 생성

    #리스트에 데이터 추가
    def add_data(self, data):
        linear = self.linear    #빈 리스트의 참조값을 변수에 넘기기
        linear.append(None)     #빈 공간 만들기
        lLen = len(linear)
        linear[lLen - 1] = data

    #데이터 삽입
    def insert_data(self, position, data):
        '''
        linear = [3,5,4,2,6]
        position = 3
        data = 99
        len(linear) == 5
        '''
        linear = self.linear

        if position < 0 or position > len(linear): #유효성 검사. 사전에 잘못된 데이터 들어오는 것 막기
            print('데이터를 삽입할 범위를 벗어났습니다.')
            return

        linear.append(None)
        linearSize = len(linear)
        '''
            linear = [3,5,4,2,6,None]
            position = 3
            data = 99
            len(linear) == 6
            '''

        for i in range(linearSize - 1, position, -1): #뒤에서부터 앞으로 이동!
            linear[i] = linear[i-1]
            linear[i-1] = None

        linear[position] = data

    #데이터 삭제
    def delete_data(self, position):
        linear = self.linear

        if position < 0 or position > len(linear):
            print('데이터를 삭제할 범위를 벗어났습니다.')

        linear[position] = None
        linearSize = len(linear)

        for i in range(position + 1, linearSize):
            linear[i - 1] = linear[i]
            linear[i] = None

        del(linear[linearSize - 1])

    #데이터 출력
    def print_list(self):
        linear = self.linear
        for list in linear:
            print(list)


#실행 코드
linear = LinearList()
linear.add_data(3)
linear.add_data(5)
linear.add_data(4)
linear.add_data(2)
linear.add_data(6)

linear.insert_data(3, 99)

linear.delete_data(2)

linear.print_list()