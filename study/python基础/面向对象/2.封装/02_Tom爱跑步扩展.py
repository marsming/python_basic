"""
Person
name
weight
__init__:
__str__:
run():
eat():
"""


class Person:

	def __init__(self, name, weight):
		self.name = name
		self.weight = weight

	def __str__(self):
		return "我是 %s 体重是 %.2f 公斤" % (self.name, self.weight)

	def run(self):
		print("%s 爱跑步，跑步锻炼身体" % self.name)
		self.weight -= 0.5

	def eat(self):
		print("%s 是吃货，吃饱才有力气减肥" % self.name)
		self.weight += 1


tom = Person("Tom", 75.0)
tom.run()
tom.eat()
print(tom)

print("-" * 50)
# Rose爱跑步
rose = Person("Rose", 45.0)
rose.eat()
rose.run()
print(rose)
