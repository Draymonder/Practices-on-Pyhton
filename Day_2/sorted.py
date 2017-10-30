L1 = [36,23,-2,13,1414,-21,3] #实数序列
L11 = ['Hello','every','One']

L2 = sorted(L1)
L3 = sorted(L1, key = abs,reverse = True) #高阶函数，关键词key、reverse可以指定函数执行原则（此次表示按绝对值大小反向排序）

L4 = sorted(L11, key = str.lower) #字符串按首字母对应ASCII码, str.lower()函数是小写处理后比较

print(L1)  # sorted函数不改变原序列 , sort()方法改变原序列
print(L2)
print(L3)
print(L4)

# 按姓名/成绩排序，例题
L = (('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88))

def by_name(t):
    print(id(t))
    t = t[0] 
    print(id(t))       #元组不可变指的是对象不变，此处t指向其他对象了，也就是映射
    return t

def by_results(t):
    t = t[1]
    return t

LL = sorted(L, key = by_name)
LLL = sorted(L, key = by_results)
print(LL)
print(LLL)
