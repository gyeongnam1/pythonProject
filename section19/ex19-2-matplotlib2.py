'''
ex19-2-matplotlib2.py
'''

import matplotlib.pyplot as plt

#figure랑 axes를 같이 객체 생성.
fig, ax = plt.subplots()

#데이터 설정
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40,100,30,55]
bar_labels = ['red', 'blue', '_red', 'orange'] #_red는 red가 반복되니까 한번만 해라
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

#막대 그래프(x축, y축, 범례(그래프 요소 설명), 바의 색깔)
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title("Fruit supply by kind and color")
ax.legend(title='Fruit color') #범례 제목 설정

plt.show()