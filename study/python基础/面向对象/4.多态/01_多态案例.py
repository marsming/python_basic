class Dog(object):

	def __init__(self,name):
		self.name = name

	def game(self):
		print("%s 玩耍..." % self.name)


class XiaoTianDog(Dog):

	def game(self):
		print("[%s] 在天上玩耍..." % self.name)


class Person(object):

	def __init__(self,name):
		self.name = name

	def game_with_dog(self,dog):
		print("%s 和 %s 玩耍..." % (self.name,dog.name))

		# 让狗玩耍
		dog.game()


# 1.创建一个狗对象
wangcai = Dog("旺财")

# 2.创建一个tom对象
tom = Person("Tom")

# 3.让tom和狗玩耍
tom.game_with_dog(wangcai)