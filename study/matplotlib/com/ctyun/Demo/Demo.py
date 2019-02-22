import matplotlib.pylab as pyl
import pandas as pd
import numpy as np


#读取execl中的数据并可视化分析
data = pd.read_excel('datas.xlsx')
#print(data.shape)   #查看数据
#print(data)
#print(data.describe())
#data.values第几行、第几列
#print(data.values[0][0:])
#转置
data1 = data.T
#print(data1)
x = data1.values[4]
y = data1.values[5]
pyl.plot(x,y)
x1 = data1.values[0]
print(x)
#pyl.plot(x1,x)
pyl.show()