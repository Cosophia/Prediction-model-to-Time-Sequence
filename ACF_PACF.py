import random as rd
from operator import index

import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf


plt.rcParams['font.family'] = 'SimHei' # 使用黑体
plt.rcParams['axes.unicode_minus'] = False # 正常显示负号
'''这里是通过调用展示ACF、PACF的趋势'''
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
    """
    :param data_ori: 原序列
    :param data_t: 当前时刻序列
    :param data_lags: 滞后序列
    :return: ACF数值
    """
    cov_data = np.cov(data_t,data_lags)[0,1]
    var_data = np.var(data_ori,ddof=1)
    return cov_data/var_data

def PACF_calculation():
    pass

if __name__ == "__main__":
    # 滞后数列表
    lags = [1,2,3]
    # 原序列
    data = np.array([12, 37, 8, 25, 41,45,37,28])
    for flag in range(len(lags)):
        '''
        flag: lags序列的下标
        '''
        # 为滞后列表预分配空间
        data_t_minus_tags = np.zeros(len(data) - lags[flag])
        # 滞后序列的构造
        for index in range(lags[flag],len(data)):
            data_t_minus_tags[index-lags[flag]] = data[index]
        print(f"Lags:{lags[flag]}滞后:",data_t_minus_tags)
        # 当前时刻序列
        data_time = data[0:(len(data) - lags[flag])]
        # ACF的计算
        ACF = ACF_calculation(data,data_time,data_t_minus_tags)
        print(f"Lags:{lags[flag]}ACF:",ACF)
    # 调用ACF进行对比验证
    plot_acf(data,lags=3)
    plot_pacf(data,lags=3)
    plt.show()

    # 一阶差分
    # 为滞后列表预分配空间
    diff_data = np.zeros(len(data)-1)
    # 滞后序列的构造
    for index in range(len(diff_data)):
        diff_data[index] = data[index+1] - data[index]
    for flag in range(len(lags)):
        data_t_minus_tags = np.zeros(len(diff_data) - lags[flag])
        for index in range(lags[flag], len(diff_data)):
            data_t_minus_tags[index - lags[flag]] = diff_data[index]
        print(f"Lags:{lags[flag]}滞后:", data_t_minus_tags)
        # 当前时刻序列
        data_time = diff_data[0:(len(diff_data) - lags[flag])]
        # ACF的计算
        ACF = ACF_calculation(diff_data,data_time, data_t_minus_tags)
        print(f"Lags:{lags[flag]}ACF:", ACF)
    # 调用ACF进行对比验证
    plot_acf(diff_data, lags=3)
    plot_pacf(diff_data,lags=3)
    plt.show()
