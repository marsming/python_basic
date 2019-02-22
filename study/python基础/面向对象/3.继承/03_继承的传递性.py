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
		print("哮天犬能腾云驾雾")


xiaotianquan = XiaoTianQuan()
xiaotianquan.eat()
xiaotianquan.run()
xiaotianquan.drink()
xiaotianquan.sleep()
xiaotianquan.bark()
xiaotianquan.fly()


"""
单继承
"""