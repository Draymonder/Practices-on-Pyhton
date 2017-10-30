
import functools

print(int('12324'))
print(sorted([23,-1,32,-133]))

int8 = functools.partial(int, base = 8)
sorted_abs = functools.partial(sorted, key = abs)

print(int8('12324'))
print(sorted_abs([23, -1, 32, -133]))   # partial()函数（偏函数）用来固定一个函数的参数


s = [2, 34, 5]
x = s          # x、s同时指向原来的[2, 34, 5]
y = s.copy()   # y指向新的(拷贝的)[2, 5, 34]，此时内存有两个[2, 5, 34]
s.sort()       # 将s指向的序列排序并原地修改  sorted()函数则不修改原来的序列
print(s)       # [2, 5, 34] 被修改
print(x)       # [2, 5, 34] 指向同一个被修改的序列
print(y)       # [2, 34, 5] 指向另一个序列，未被修改