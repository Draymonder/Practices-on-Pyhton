def count1():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs    #返回函数不要引用任何循环变量，或者后续会发生变化的变量（这里造成错误）。

f1,f2,f3 = count1()
print(f1()) # 9
print(f2()) # 9
print(f3()) # 9
#原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

#解决方法
def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1,f2,f3 = count2()
print(f1()) # 1
print(f2()) # 4
print(f3()) # 9