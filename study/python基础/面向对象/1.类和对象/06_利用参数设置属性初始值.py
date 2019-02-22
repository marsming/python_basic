class Cat:

	def __init__(self, new_name):
		self.name = new_name

	def eat(self):
		print("%s 爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法__init__
tom = Cat("Tom")
tom.eat()
print(tom.name)
