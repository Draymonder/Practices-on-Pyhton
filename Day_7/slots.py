from types import MethodType

class Student(object):
    # 用__slots__变量限制能添加的属性 
    __slots__ = ("name", "age", "set_age")  # 只对当前类实例有用，不能用于继承类
 
def set_age(self, age):
    self.age = age


s1 = Student()
s1.name = "Chengkang"   #动态绑定属性
s1.set_age = MethodType(set_age, s1)#动态绑定方法

s1.set_age(24) #调用方法

print('%s: %s' % (s1.name, s1.age)) # Output:Chengkang: 24

# 对其他对象不起作用
s2 = Student()
#s2.set_age(25)  报错'Student' object has no attribute 'set_age'

# 解决办法：给类绑定方法
Student.set_age = set_age
s3 = Student()
s3.set_age(23)
s2.set_age(25)

print(s2.age + s3.age) # Output: 48
