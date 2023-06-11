'''
ex13-9-readHello6.py
'''

import sys

with open('hello.txt', 'rt', encoding = 'UTF-8') as file:
    line_list = file.readlines()
    sys.stdout.writelines(line_list) #print 대신 쓸 수 있음. 콘솔에 출력해주겠다.