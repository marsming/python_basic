import os,shutil,re
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

'''
为美国风格的日期创建一个正则表达式
MM-DD-YYYY
'''
if __name__ == '__main__':

    datePattern = re.compile(r'''
    ^(.*?)          #任意字符串开头
    ((0|1)?\d)-     #一个或两个数字代表月
    ((0|1|2|3)?\d)- #一个或两个数字代表天
    ((19|20)\d\d)   #四位数字代表年
    (.*?)$
    ''', re.VERBOSE)

    #识别文件名中的日期部分
    for fileName in os.listdir('../../../datas'):
        mo = datePattern.search(fileName)

        if mo == None:
            continue
        beforePart = mo.group(1)
        monthPart = mo.group(2)
        dayPart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(8)

        #构成新文件名，并对文件改名
        newFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
        WorkingDir = os.path.abspath('../../../datas')      #获取当前文件路径
        fileName = os.path.join(WorkingDir,fileName)
        newFileName = os.path.join(WorkingDir,newFileName)

        print('Renaming "%s" to "%s"...' % (fileName,newFileName))
