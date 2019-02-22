class A:

	def __init__(self):
		self.num = 100
		self.__num2 = 200

	def __test(self):
		print("私有方法 %d %d" % (self.num,self.__num2))

	def test(self):
		print("父类的公有方法 %d" % self.__num2)
		self.__test()

class B(A):

	def demo(self):

		# 1.在子类的对象方法中，不能访问父类的私有属性
		# print("访问父类的私有属性 %d " % self.__num2)
		# 2.在子类的对象方法中，不能调用父类的私有方法
		# self.__test()
		# 3.访问父类的公有属性
		print("子类方法 %d" % self.num)
		# 4.调用父类的公有方法
		self.test()


# 创建子类对象
b = B()
b.demo()
# 在外界访问父类的公有属性或公有方法
# b.test()