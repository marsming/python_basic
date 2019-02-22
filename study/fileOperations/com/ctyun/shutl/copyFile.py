import shutil
import os
##复制文件和文件夹
#查看当前工作目录
print(os.getcwd())
print(os.chdir('C:\\'))
print(os.getcwd())

#当前工作目录为C盘根目录
shutil.copy('C:\\kms10.log','C:\\test')  #拷贝文件
shutil.copy('C:\\kms10.log','C:\\test\\kms10.log.bak')  #拷贝并修改文件名
