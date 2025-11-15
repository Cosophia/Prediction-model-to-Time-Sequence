import random as rd
from operator import index

import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf


plt.rcParams['font.family'] = 'SimHei' # 使用黑体
plt.rcParams['axes.unicode_minus'] = False # 正常显示负号
'''这里是通过调用看ACF、PACF的趋势'''
# # 预分配
# lags = [1,2,3]
# data = np.array(np.random.randint(-10,40,size=80))
# print("预分配:",data)
# plot_acf(data)
# plot_pacf(data,lags=40)
# plt.show()
#
#
# # 执行一阶差分
# diff_data = np.zeros(data.size-1)
# for index in range(len(diff_data)):
#     diff_data[index] = data[index+1] - data[index]
# print("一阶差分序列:",diff_data)
# diff_data = np.array(diff_data)
# plot_acf(diff_data)
# plot_pacf(diff_data)
# plt.show()


'''手动计算ACF和PACF,这里仅仅以lags = [1,2,3]中为例子'''
def ACF_calculation(data_ori,data_t,data_lags):
    cov_data = np.cov(data_t,data_lags)[0,1]
    var_data = np.var(data_ori,ddof=1)
    return cov_data/var_data

def PACF_calculation():
    pass

if __name__ == "__main__":
    lags = [1,2,3]
    data = np.array([12, 37, 8, 25, 41,45,37,28])
    # 原序列
    for flag in range(len(lags)):
        data_t_minus_tags = np.zeros(len(data) - lags[flag])
        for index in range(lags[flag],len(data)):
            data_t_minus_tags[index-lags[flag]] = data[index]
        print(f"Lags:{lags[flag]}滞后:",data_t_minus_tags)
        ACF = ACF_calculation(data,data[0:(len(data) - lags[flag])],data_t_minus_tags)
        print(f"Lags:{lags[flag]}ACF:",ACF)
    plot_acf(data,lags=3)
    plot_pacf(data,lags=3)
    plt.show()

    # 一阶差分
    diff_data = np.zeros(len(data)-1)
    for index in range(len(diff_data)):
        diff_data[index] = data[index+1] - data[index]
    for flag in range(len(lags)):
        data_t_minus_tags = np.zeros(len(diff_data) - lags[flag])
        for index in range(lags[flag], len(diff_data)):
            data_t_minus_tags[index - lags[flag]] = diff_data[index]
        print(f"Lags:{lags[flag]}滞后:", data_t_minus_tags)
        ACF = ACF_calculation(diff_data,diff_data[0:(len(diff_data) - lags[flag])], data_t_minus_tags)
        print(f"Lags:{lags[flag]}ACF:", ACF)
    plot_acf(diff_data, lags=3)
    plot_pacf(diff_data,lags=3)
    plt.show()
