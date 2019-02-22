from faker import Faker
import pandas as pd
import numpy as np

def data(s):
    faker = Faker('zh_CN')
    datas = []
    for i in range(1,s+1):
        name = faker.name()
        city = faker.city()
        url = faker.url()
        click = faker.random.randint(2000,3000)
        read = faker.random.randint(0,500)
        data = [name,city,url,click,read]
        datas.append(data)
    #print(datas)
    return datas

def to_execl(s):
    #将矩阵装置
    arr = np.array(data(s)).T
    print(arr)
    df = pd.DataFrame()
    df['name']=arr[0]
    df['city']=arr[1]
    df['url']=arr[2]
    df['click']=arr[3]
    df['read']=arr[4]
    df.to_excel('datas.xlsx',index_label='num')

to_execl(5000)



