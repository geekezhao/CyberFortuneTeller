
Move = 23
Emotion = 28
Intelligence = 33

import datetime
current = datetime.date.today()
birthday = datetime.date(1997, 1, 9)
current_minus = datetime.date.today() - datetime.timedelta(days=15)
current_plus = datetime.date.today() + datetime.timedelta(days=15)

duration_minus = (current_minus - birthday).days
duration_plus = (current_plus - birthday).days
duration = (current - birthday).days

# print(current)
# print(birthday)
print(duration)
print(type(duration))
# print(current_minus)


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# print(np.sin(0))
def sinplot(flip = 1):
    x = np.linspace(duration_minus, duration_plus, 30)
    print(x)
    print(np.sin(np.pi*2*(x-x//Move*Move))*flip)
    # for i in range(1, 6):
    plt.plot(x, np.sin(np.pi*2*(x%Move)/Move)*flip, label='Energy')
    plt.plot(x, np.sin(np.pi*2*(x%Emotion)/Emotion)*flip, label='Mood')
    plt.plot(x, np.sin(np.pi*2*(x%Intelligence)/Intelligence)*flip, label='Intelligence')
    # plt.plot(x=16)
    plt.axvline(x=15+duration_minus, color='black', linewidth=1.0, linestyle='--')

    # 设置坐标轴刻度
    # my_x_ticks = [current_minus, current, current_plus]
    # 对比范围和名称的区别
    # my_x_ticks = np.arange(-5, 2, 0.5)
    xticks_labels = ['{}'.format(i) for i in [current_minus, current, current_plus]]
    # 修改横坐标的刻度,并且为横坐标上的每个刻度添加标签
    plt.xticks(np.linspace(duration_minus,duration_plus,3,endpoint=True),xticks_labels)
    # my_y_ticks = np.arange(-2, 2, 0.3)
    # plt.xticks(my_x_ticks)
    # plt.yticks(my_y_ticks)

    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()

    # plt.show()
    plt.savefig('current_period.jpg')
#
sinplot()

