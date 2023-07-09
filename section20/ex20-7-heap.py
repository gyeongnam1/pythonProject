'''
ex20-7-heap.py

힙(heap) - 데이터 저장소의 힙과 완전 다른 아이임.
    최대값 및 최소값을 찾아내는 연산을 빠르게 하기 위해 고안된
    완전 이진트리를 기본으로한 자료 구조
'''

import heapq

class Minheap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, val)

    def pop(self):
        return heapq.heappop(self.heap)

#실행 코드
heap = Minheap()
heap.push(3)
heap.push(1)
heap.push(4)
heap.push(2)

print('>>>>>>>>>>>>>>>>>>>>MinHeap<<<<<<<<<<<<<<<<<<<<')
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
#해보면 정렬해서 나옴

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, -val) #마이너스 먹여주기!

    def pop(self):
        return -heapq.heappop(self.heap) #마이너스 다시 곱해서 프린트하기

#실행 코드
heap = MaxHeap()
heap.push(3)
heap.push(1)
heap.push(4)
heap.push(2)

print('>>>>>>>>>>>>>>>>>>>>MaxHeap<<<<<<<<<<<<<<<<<<<<')
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())