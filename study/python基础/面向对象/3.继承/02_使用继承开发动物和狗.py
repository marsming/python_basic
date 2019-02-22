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


class Cat(Animal):

	def catch(self):
		print("抓鱼")


wangcai = Dog()
wangcai.eat()
wangcai.run()
wangcai.drink()
wangcai.sleep()
wangcai.bark()

"""
单继承
"""
