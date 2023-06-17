'''
ex14-8-jsonReader.py
'''

import json
with open('dictList.json', 'r', encoding='UTF-8') as file:
    json_reader = file.read() #파일을 읽고
    dict_list = json.loads(json_reader) #파일의 값을 loads를 사용해서 dict_list에 넣음

for dic in dict_list:
    print('이름: {}'.format(dic['name']))
    print('나이: {}'.format(dic['age']))
    print('키: {}'.format(dic['spec'][0]))
    print('몸무게: {}'.format(dic['spec'][1]))
    print()