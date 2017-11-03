
import numpy as np
from math import pi
import matplotlib.pyplot as plt
Sum = 0
list = []
list_float = []
Offset_list_float = []
Total_list = []
#读取每一行放在列表list里，列表第一个元素为空格
filename = 'data3.txt'
with open(filename) as file_object:
	for lines in file_object:
		list.append(lines.strip())


#转为float型
for i in range(1, len(list)):
	list_float.append(float(list[i]))

#返回差值列表,长度减一
def Delta_List(L):
	Delta_L = []
	for i in range(len(L)-1):
		Delta_L.append(L[i+1] - L[i])
	return Delta_L

#2pi补偿函数
def Offset(delta):
	if abs(delta) < pi : 
		return 0
	elif delta > pi and delta <= 2*pi:
		return -2*pi
	else:
		return 2*pi


#创建补偿数组

for i in range(len(Delta_List(list_float))+1):
	if i == 0 : 
		Offset_list_float.append(Sum);
		continue;
	else:
		Sum += Offset(Delta_List(list_float)[i-1]) #差值列表每一项作补偿判断并对前面的序列求和
		Offset_list_float.append(Sum)

#正确序列
for i in range(len(list_float)):
	Total_list.append(list_float[i]+Offset_list_float[i])




plt.plot(Total_list,'-o', ms=0, lw=1.5, alpha=0.7, mfc='orange')
plt.xlabel('Sample')
plt.ylabel('Phase')
plt.show()


