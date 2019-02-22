class Cat:

	def eat(self):
		print("%s 爱吃鱼" % self.name)

	def drink(self):
		print("%s 要喝水" % self.name)


# 创建猫对象
tom = Cat()

# 可以使用 .属性名 利用赋值语句即可
tom.name = "Tom"

tom.eat()
tom.drink()  