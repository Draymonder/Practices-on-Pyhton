#!/usr/bin/python
# -*- coding: UTF-8 -*-

from functools import reduce

str1 = '358358'

#将字符串转为整数
def StrToInt(str):
	#将字符序列'358358'或['3','5','8','3','5','8'] 转为 整数序列[3,5,8,3,5,8] 
	def StrToIntList(k):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[k]   #k键是字符串
	IntList = list(map(StrToIntList,str))  #map返回一个迭代器，用List函数转为一个List

	#将整数序列[3,5,8,3,5,8] 转为 整数358358
	#方法一
	def ListToValue(x,y):
		return x*10+y
	IntValue = reduce(ListToValue,IntList)  #reduce返回一个值
	return IntValue
	#方法二
	return reduce(lambda x,y:x*10+y,IntList)

print(StrToInt(str1))
print(int(str1))#Python自带函数