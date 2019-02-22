import numpy as np
import pandas as pd

#将数据按日转换成多列（列转行）
df = pd.read_excel("./data_trans/data.xlsx")
print(df.__len__())
#print(df)
print(type(df.__len__()))
list1 = [x for x in range(0,df.__len__(),10)]
values = []
for i in list1:
    list2 = [x for x in range(i,i+10)]
    values = [df['count'].loc[list2].tolist()]
    #print(list2)
    #print(values)
    print("===========")
