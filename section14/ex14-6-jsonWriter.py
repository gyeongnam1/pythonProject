'''
ex14-6-jsonWriter.py

JSON (JavaScript Object Notation)
    데이터를 키와 값의 쌍으로 중괄호({})로 묶어 표현하는 형식
    - 딕셔너리와 비슷하다.
    - 구조 { K : V }
'''

import json

dict_list = [ #리스트 안에 딕셔너리가 2개 들어있음.
    {
        'name':'james',
        'age':20,
        'spec':[
            175.5,
            70.5
        ]
    },
    {
        'name':'Alice',
        'age':21,
        'spec':[
            168.5,
            60.5
        ]
    }
]

json_string = json.dumps(dict_list)

with open('dictList.json', 'w') as file:
    file.write(json_string)
print('dictList.jason 파일이 생성되었습니다')
#csv랑 거의 비슷한데 가끔 서버끼리 통신할 때 csv를 읽지 못할 때가 있음.
#그래서 좀 더 명확하게 key값이 같이 있는 json을 쓰기도 함.
#즉 서버에 있는 데이터를 통신할 때는 json, 파일을 읽고 쓸 때는 csv