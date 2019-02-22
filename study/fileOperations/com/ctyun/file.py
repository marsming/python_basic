import os

#读取文件
file1 = open('../../datas/a.txt','r',encoding='utf-8')
readFile1 = file1.read()
print(readFile1)
file1.close()

#写入文件
file2 = open('../../datas/b.txt','w',encoding='utf-8')
writeFile2 = file2.write(readFile1)
file2.close()