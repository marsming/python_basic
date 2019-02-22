class Animal:

	def eat(self):
		print("吃")

	def drink(self):
		print("喝")

	def run(self):
		print("跑")

	def sleep(self):
		print("睡")


class Dog(Animal):

	def bark(self):
		print("汪汪叫...")


class XiaoTianQuan(Dog):

	def fly(self):
		print("哮天犬能腾云驾雾...")

	# 对父类方法的扩展
	def bark(self):
		# 1.针对子类特有的需求编写
		print("哮天犬叫...")
		# 2.使用super()，调用原本父类中封装的方法
		super().bark()
		# 3.增加其他子类的代码
		print("*" * 10)


xtq = XiaoTianQuan()
xtq.bark()
xtq.fly()