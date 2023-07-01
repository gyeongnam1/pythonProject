'''
ex19-3-matplotlib3.py
'''

from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

font_path = 'C:\Windows\Fonts\malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font',family=font_name)

figure = plt.figure()
axes = figure.add_subplot(111)
data = [0.18, 0.3, 3.33, 3.75, 0.38, 25, 0.25, 2.75, 0.1]
vitamin = ['비타민A', '비타민B1', '비타민B2', '나이아신', '비타민B6', '비타민C', '비타민D', '비타민E', '엽산']
axes.pie(data, labels=vitamin, autopct='%0.1f%%') #소수점 한자리까지 표현. %로 나오게 %를 2개 쓴 것
plt.axis('equal') #가로 세로 비율 동일
plt.show()
