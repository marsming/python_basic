class HouseItem:
	def __init__(self, name, area):
		self.name = name
		self.area = area

	def __str__(self):

		return "[%s]占地 %.2f 平米" % (self.name, self.area)


# 创建家具
bed = HouseItem("席梦思", 4)
print(bed)
chest = HouseItem("衣柜", 2)
print(chest)
table = HouseItem("餐桌", 1.5)
print(table)
