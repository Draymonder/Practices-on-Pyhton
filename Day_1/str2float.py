# -*- coding: utf-8 -*-

from functools import reduce

CHAR_TO_FLOAT = {
	'0':0,
	'1':1,
	'2':2,
	'3':3,
	'4':4,
	'5':5,
	'6':6,
	'7':7,
	'8':8,
	'9':9,
	'.':-1,
}

def str2float(s):
    nums = list(map(lambda ch: CHAR_TO_FLOAT[ch], s)) # nums = [1,2,3,-1,4,5,6]
    point = nums.index(-1)
    nums.pop(point)
    length = len(nums[point:])
    return reduce(lambda x,y: x*10+y,nums)/(pow(10,length))

print(str2float('213123123.123123'))
