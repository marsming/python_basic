from faker import Faker
import pandas as pd
import numpy as np

def dataList(s):
    faker = Faker('zh_CN')
    names = []
    city = []
    age = np.random.randint(20,60,size=s).tolist()
    height = np.random.randint(160,190,size=s).tolist()
    weight = np.random.randint(100,160,size=s).tolist()
    for i in range(1,s+1):
        names.append(faker.name())
        city.append(faker.city())
    dict = {
        'name':names,
        'city':city,
        'age':age,
        'height':height,
        'weight':weight
    }
    return dict



def to_execl(num):
    #print(dataList(10))
    df = pd.DataFrame(dataList(num), columns=['name', 'city', 'age', 'height','weight'])
    df.to_excel('people.xlsx')


if __name__ == '__main__':
    to_execl(500)


