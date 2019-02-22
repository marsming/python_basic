import os

if __name__ == '__main__':
    #sonnetFile = open('D:\myProject\Python\study\datas\sonnet.txt')
    #print(sonnetFile.readlines())

    baconFile = open('D:\\myProject\\Python\\study\\Regex\\datas\\bacon.txt','w')
    baconFile.write('hello world!\n')
    baconFile.close()
    baconFile = open('D:\\myProject\\Python\\study\\Regex\\datas\\bacon.txt','a')
    baconFile.write('Bacon is not a vegetable!')
    baconFile.close()
    baconFile = open('D:\\myProject\\Python\\study\\Regex\\datas\\bacon.txt')
    content = baconFile.read()
    baconFile.close()
    print(content)
