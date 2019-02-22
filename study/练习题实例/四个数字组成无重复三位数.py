
'''
简述：这里有四个数字，分别是：1、2、3、4
提问：能组成多少个互不相同且无重复数字的三位数？各是多少？
'''

list1 = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            num = i * 100 + j * 10 + k
            list1.append(num)

print(list1)
print(list1.__len__())
