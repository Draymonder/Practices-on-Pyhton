class Student():
	def __init__(self , name, score):
		#self.name = name
		self.__name = name  #相当于加了个private,外部不能访问
		#self.score = score
		self.__score = score

	def print_score(self):
		print("%s,%s" % (self.__name,self.__score))

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

#封装,用get和set访问与修改
	def set_name(self, name):
		self.__name = name

	def set_score(self, score):
		self.__score = score

ck = Student('chengkang', 79)
ck.print_score()
#print(ck.__name) #报错,因为__name私有
print(ck.get_name())
ck.set_score(100)
#或者
#ck._Student__score = 100 #内部__score被改为_Student__score
print(ck.get_score())



