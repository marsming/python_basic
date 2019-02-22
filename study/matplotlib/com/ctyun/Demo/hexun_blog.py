from faker import Faker
import pandas as pd

def dataList(s):
    faker = Faker('zh_CN')
    names = []
    url = []
    city = []
    click = []
    num = []
    for i in range(1,s+1):
        num.append(i)
        names.append(faker.name())
        url.append(faker.url())
        city.append(faker.city())
        click.append(faker.pyint())
    dict = {
        'num':num,
        'name':names,
        'url':url,
        'city':city,
        'click':click
    }
    #print(dict)
    return dict



def to_execl():
    df = pd.DataFrame(dataList(5000), columns=['name', 'city', 'url', 'click'])
    df.to_excel('hexun_blog.xlsx',index_label='num')

#print(dataList(10))
to_execl()