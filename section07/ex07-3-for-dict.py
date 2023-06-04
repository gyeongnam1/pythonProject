'''
ex07-3-for-dict.py

for 문과 dict
'''

eng_dict = {
    'sun':'태양',
    'moon':'달',
    'star':'별',
    'space':'우주'
}
for word in eng_dict: #value가 아니라 key값을 word에 넣음.
    print('{}의 뜻 : {}'.format(word, eng_dict.get(word)))
for word in eng_dict:  # value가 아니라 key값을 word에 넣음.
    print('{}의 뜻 : {}'.format(word, eng_dict[word]))

print("======================================")

eng_dict_keys = eng_dict.keys()
for k in eng_dict_keys:
    print("eng_dict의 key: {}".format(k))