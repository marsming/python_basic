class Woman:

	def __init__(self,name):
		self.name = name
		self.__age = 20

	def __secret(self):
		# 在对象的方法内部是能访问对象的私有属性的
		print("%s 的年龄是 %d " % (self.name , self.__age))


xiaomei = Woman("小美")

# 在名称前面加上	_类名 => _类名__名称

print(xiaomei._Woman__age)

xiaomei._Woman__secret()