import os

#当前工作目录
src = os.getcwd()
print('当前工作目录：',src)

#创建新文件夹
#os.mkdir('../../datas/test')

#查看文件大小和文件夹内容
#调用 os.path.getsize(path)将返回 path 参数中文件的字节数
fileSize = os.path.getsize('../../datas/a.txt')
print(fileSize)

#调用 os.listdir(path)将返回文件名字符串的列表，包含 path 参数中的每个文件
files = os.listdir('../../datas')
print(files)
