import shelve

#shelve模块保存变量
#常用来保存Python程序中的数据

shelfFile = shelve.open('../../datas/mydata')
cats = ['Tom','Pooka','Simon']

#将列表cats赋值给shelFile
#shelfFile['cats'] = cats

print(type(shelfFile))
cats_1 = shelfFile['cats']
print(cats_1)
shelfFile.close()