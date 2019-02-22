import re

# TODO:强口令检测
'''
长度不少于 8 个字符， 同时包含大写和小写字符， 至少有一位数字
'''



def checkpw():
    text = str(input('输入一串口令：'))
    flag = True
    if len(text) < 8:
        #flag = False
        return False
    else:
        chpw1 = re.compile(r'[a-z]').search(text)         #包含小写字母
        chpw2 = re.compile(r'[A-Z]').search(text)         #包含大写字母
        chpw3 = re.compile(r'[0-9]').search(text)         #包含数字
        if (chpw1 == None) or (chpw2 == None) or (chpw3 == None):  #如果不存在字母数字
            flag = False
        if flag:
            #print('口令符合')
            return True
        else:
            #print('口令不符合')
            return False

if __name__ == '__main__':
    while True:
        flag = checkpw()
        #print(checkpw(text))
        if flag:
            print('口令符合')
            break
        else:
            print('口令不符合')
