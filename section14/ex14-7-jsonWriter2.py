'''
ex14-7-jsonWriter2.py
'''
import json

dict_list = [
    {
        'name':'James',
        'age':20,
        'spec':[
            175.5,
            70.5
        ]
    },
    {
        'name':'홍길동',
        'age':21,
        'spec':[
            165,
            52
        ]
    }
]
json_string = json.dumps(dict_list, indent=4, ensure_ascii=False)
with open('dictList.json', 'w', encoding='UTF-8') as file:
    file.write(json_string)
print('dictList.json 파일이 생성되었습니다.')
