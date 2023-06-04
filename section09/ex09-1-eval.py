'''
ex09-1-eval.py

내장 함수
    별도의 임포트 없이 어디서든 사용할 수 있는 함수

eval() 함수
    매개변수로 받은 expression(=식)을
    문자열로 받아서 실행하는 함수
'''
expr = input("계산식을 입력하세요 >>> ")
result = eval(expr)
print(expr, '=', str(result))
#result를 str로 캐스팅하는 이유는 [지금은 안 해도 되는데(구분이 ,라서)]
#만약 구분이 +이면 문자열로 연결해야하니까 str로 습관적으로 붙임.