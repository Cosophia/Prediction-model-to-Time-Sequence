import random as rd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei' # 使用黑体
plt.rcParams['axes.unicode_minus'] = False # 正常显示负号

# 预分配
lags = [1,2,3]
data = [0]*25
print("预分配:",data)

# 随机生成时间序列值
for index in range(len(data)):
    data[index] = rd.randint(-10,40)
print("随机生成时间序列值:",data)

'''在Differential.py中,我们做的是滞后项为1的高阶差分,现在我们对改变滞后项(即步长)'''
# 执行滞后项为[1,2,3]各自的一、二、三阶差分
for tag in range(len(lags)):
    # 一阶差分
    diff_data = [0] * (len(data)-(lags[tag]+1))
    for index in range(len(diff_data)):
        diff_data[index] = data[index+lags[tag]] - data[index]
    print(f"lags为{lags[tag]}的一阶差分序列:",diff_data)
    # 二阶差分
    diff_data_2 = [0] * (len(diff_data) - (lags[tag] + 1))
    for index in range(len(diff_data_2)):
        diff_data_2[index] = diff_data[index+lags[tag]] - diff_data[index]
    print(f"lags为{lags[tag]}的二阶差分序列:",diff_data_2)
    # 三阶差分
    diff_data_3 = [0] * (len(diff_data_2) - (lags[tag] + 1))
    for index in range(len(diff_data_3)):
        diff_data_3[index] = diff_data_2[index + lags[tag]] - diff_data_2[index]
    print(f"lags为{lags[tag]}的三阶差分序列:", diff_data_3)
    print('-' * 150)


