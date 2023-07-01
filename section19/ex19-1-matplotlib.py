'''
ex19-1-matplotlib.py

데이터 시각화(data visualization)
    데이터를 분석한 결과를 사용자가 쉽게 이해할 수 있도록
    표현하여 전달한 것을 의미한다.
    = 표 만들어주는 것
'''

import matplotlib.pyplot as plt

#figure 객체 생성
figure = plt.figure() #그래프 그려주는 창 = figure
axes = figure.add_subplot(111) #행, 열, 번호. 즉 1행 1열 첫번째 칸으로 보여주겠다.
#222로 하면 그래프가 작아지면서 분할된 사사분면에서 2번째 칸에 나옴.
x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
y = [1200, 800, 500, 400, 700, 800]
axes.plot(x,y, linestyle='--', marker='^', color='red')
plt.show()