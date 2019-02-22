import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pformat_1 = pprint.pformat(cats)
print(pformat_1)

file = open('../../datas/myCats.py', 'w')
file.write('cats = '+pformat_1 + '\n')
file.close()