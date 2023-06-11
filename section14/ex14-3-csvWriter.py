'''
ex14-3-csvWriter.py
'''

import csv

#첫번째 방법
'''
with open('차량관리.csv', 'w', encoding='UTF-8') as file:
    csv_maker = csv.writer(file,delimiter=',') #writer가 import csv에 있는 기능인 듯.
    csv_maker.writerow([1, '08러1234', '2023-06-11, 12:00'])
    csv_maker.writerow([2, '25다1234', '2023-06-11, 12:10'])
    csv_maker.writerow([3, '28하1234', '2023-06-11, 12:20'])
print('차량관리.csv 파일이 생성되었습니다.')

#두번째 방법. 개행을 없애고 싶을 때 
with open('차량관리.csv', 'w', newline='', encoding='UTF-8') as file:
    csv_maker = csv.writer(file,delimiter=',') 
    csv_maker.writerow([1, '08러1234', '2023-06-11, 12:00'])
    csv_maker.writerow([2, '25다1234', '2023-06-11, 12:10'])
    csv_maker.writerow([3, '28하1234', '2023-06-11, 12:20'])
print('차량관리.csv 파일이 생성되었습니다.')
'''
#세 번째 방법. 따옴표가 없어져서 그 안에 쉼표 때문에 하나의 요소가 두 개의 요소로 잘못 인식될 때
with open('차량관리.csv', 'w', newline='', encoding='UTF-8') as file:
    csv_maker = csv.writer(file,delimiter=',', quotechar='"')
    #근데 원래 default 값이 quotechar='"'
    csv_maker.writerow([1, '08러1234', '2023-06-11, 12:00'])
    csv_maker.writerow([2, '25다1234', '2023-06-11, 12:10'])
    csv_maker.writerow([3, '28하1234', '2023-06-11, 12:20'])
print('차량관리.csv 파일이 생성되었습니다.')