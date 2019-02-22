class Woman:

	def __init__(self,name):
		self.name = name
		self.__age = 20

	def __secret(self):
		# 在对象的方法内部是能访问对象的私有属性的
		print("%s 的年龄是 %d " % (self.name , self.__age))


xiaomei = Woman("小美")

# 私有属性在外界不能被直接访问
# print(xiaomei.__age)

# 私有方法同样不允许在外界访问
# xiaomei.__secret()