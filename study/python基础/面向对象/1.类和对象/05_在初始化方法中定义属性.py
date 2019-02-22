class Cat:

	def __init__(self):
		self.name = "Tom"


# 使用类名()创建对象的时候，会自动调用初始化方法__init__
tom = Cat()

print(tom.name)
