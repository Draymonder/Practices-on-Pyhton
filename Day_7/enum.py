from enum import Enum, unique

#实例化一个枚举类型
M = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 
    'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in M.__members__.items():
    print(name, '=>', member, ',', member.value)

# 继承枚举类
@unique #成员名称和值都不可重复
class Weekday1(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday1["Sun"].value)  #通过成员名获取成员对象的值
print(Weekday1(0).name)  #通过成员值获取成员对象名称
print(Weekday1.Mon.value, Weekday1.Mon.name)  #通过成员对象获取其值和名称
print(Weekday1.Mon == Weekday1.Sun)# False

#迭代
for member in Weekday1:
    print(member)  #打印成员对象
    print(member.name,":", member.value) #打印成员对象的名称和值

for name, member in Weekday1.__members__.items():
    print(member)  #打印成员对象
    print(name)  #打印成员对象的名称
# 成员名称不可重复，值可以
class Weekday2(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 0
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekday2["Sun"].value)
print(Weekday2.Mon.value)
print(Weekday2.Mon == Weekday2.Sun) #值相等时，两个成员是同一个对象，这里返回True

#有重复，只打印重复值的第一个
for member in Weekday2:
    print(member)  #打印成员对象
    print(member.name,":", member.value) #打印成员对象的名称和值
