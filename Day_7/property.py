class Student(object):
    #@property装饰器将方法变成属性调用，本身又创建了另一个装饰器@score.setter，可以限制赋值，避免属性的暴露
    @property
    def score(self):
        return self._score

    @property
    def name(self):
        return "chengkang"

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
#s.score = "2" #报错
print(s.name) 
#s.name = "CK" #报错，未定义setter方法。这里@property起到了只读的作用
