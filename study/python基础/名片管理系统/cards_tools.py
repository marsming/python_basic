# 记录所有名片字典
card_list = []


def show_menu():
	"""显示菜单"""
	print("*" * 50)
	print("欢迎使用【名片管理系统】V1.0")
	print()
	print("1.新建名片")
	print("2.显示全部")
	print("3.查询名片")
	print()
	print("0.退出系统")
	print("*" * 50)


def new_card():
	"""新增名片"""
	print("-" * 50)
	print("新增名片")
	# 1.提示用户输入名片信息
	name = input("请输入姓名：")
	phone = input("请输入电话：")
	qq = input("请输入QQ：")
	email = input("请输入邮箱：")

	# 2.使用用户输入的信息建立一个名片字典
	card_dict = {"name": name,
				 "phone": phone,
				 "qq": qq,
				 "email": email}
	# 3.将名片字段添加到列表中
	card_list.append(card_dict)
	# 4.提示用户添加成功
	print("添加 %s 的名片成功！" % name)


def show_all():
	"""显示所有名片"""
	print("-" * 50)
	print("显示所有名片")

	# 判断是否存在名片记录，没有提示用户并且返回
	if len(card_list) == 0:
		print("请先添加名片！")
		return None

	# 打印表头
	for name in ['姓名', '电话', 'QQ', '邮箱']:
		print(name, end='\t\t')
	print("")
	# 打印分割线
	print("=" * 50)
	# 遍历名片列表
	for card_dict in card_list:
		print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))


def search_card():
	"""查询名片"""
	print("-" * 50)
	print("查询名片")

	# 1.提示用户输入要搜索的姓名
	find_name = input("请输入要搜索的姓名：")

	# 2.遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
	for card_dict in card_list:
		if card_dict["name"] == find_name:
			print("姓名\t\t电话\t\tQQ\t\t邮箱")
			print("=" * 50)
			print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))

			break
	else:
		print("没有找到 %s " % find_name)