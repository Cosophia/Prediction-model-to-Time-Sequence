import random as rd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei' # 使用黑体
plt.rcParams['axes.unicode_minus'] = False # 正常显示负号

# 预分配
data = [0]*15
print("预分配:",data)

# 随机生成时间序列值
for index in range(len(data)):
    data[index] = rd.randint(-10,40)
print("随机生成时间序列值:",data)

# 执行一阶差分
diff_data = [0]*14
for index in range(len(diff_data)):
    diff_data[index] = data[index+1] - data[index]
print("一阶差分序列:",diff_data)

# 执行二阶差分
diff_data_2 = [0]*13
for index in range(len(diff_data_2)):
    diff_data_2[index] = diff_data[index+1] - diff_data[index]
print("二阶差分序列:",diff_data_2)

# 将原序列和差分序列生成出来
plt.figure(figsize=(10,12))
plt.plot(range(len(data)),data,label="原序列")
plt.plot(range(len(diff_data)),diff_data,label="一阶差分序列")
plt.plot(range(len(diff_data_2)),diff_data_2,label="二阶差分序列")
plt.legend()
plt.title("原序列和差分序列的对比")
plt.xlabel("时间点")
plt.ylabel("值")
plt.show()