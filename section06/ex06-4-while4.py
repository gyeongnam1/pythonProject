'''
ex06-4-while4.py

반복문 안의 반복문

*숙제
    2×1=2 3×1=3 4×1=4
    ...
    2×9=18 3×9=27 4×9=36
    5×1=5 6×1=6 7×1=7
    ...
    5×9=45 6×9=54 7×9=63
    8×1=8 9×1=9
    ...
    8×9=72 9×9=81

'''
dan = 2
while dan <= 9:
    n = 1
    while n<=9:
        print('{}×{}={} '.format(dan, n, dan*n), end='')
        n += 1
    dan += 1
    print() #개행