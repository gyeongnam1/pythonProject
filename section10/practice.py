# replace() 메소드 - 문자열 치환
s = 'life is too short'
result = s.replace('short', 'long')
print(result)

#strip(), lstrip(), rstrip() 공백제거 메소드
s = '       apple'
result = s.lstrip()
print(result)

s = 'apple            '
result = s.rstrip()
print(result)

s = '    apple      '
result = s.strip()
print(result)

s=' a p p l e  '
result = s.strip()
print(result) #띄어쓰기 제거 안됨

s = '        apple        '
result = s.replace(' ', '')
print(result)

