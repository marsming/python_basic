import json

import requests
import requests.exceptions
import re
import pandas as pd

'''
爬取豆瓣阅读中的短篇写作的：作品名+类型+作者+时间
'''


# 发送请求
def get_one_page(url):
    try:
        response = requests.get(url)
        if (response.status_code == 200):
            return response.text
        return None
    except requests.exceptions.RequestException:
        return None


# 通过正则表达式获取想要的信息：
def parse_one_page(html):
    pattern = re.compile(
        '<li.*?essay-item.*?>.*?info.*?<a.*?>(.*?)</a>.*?author.*?>(.*?)</a>.*?<time>(.*?)</time>.*?intro-text.*?>(.*?)</div>.*?</li>')
    items = re.findall(pattern, html)
    # print(items)

    for item in items:
        yield {
            'bookname': item[0],
            'author': item[1],
            'time': item[2],
            'intro': item[3]
        }


# 将信息写入到文件：
def write_to_file(content):
    file = open('result01.txt', 'a', encoding='utf-8')
    file.write(content + '\n')
    file.close()


# 主函数：
def main(offset):
    url = "https://read.douban.com/tag/%E6%B8%B4%E6%9C%9B%E4%B9%8B%E7%89%A9/?cat=all&sort=hot&start=" + str(offset)
    html = get_one_page(url)
    parse_one_page(html)
    for item in parse_one_page(html):
        print(item)
        #write_to_file(item)


if __name__ == '__main__':
    for i in range(1, 50):
        main(i)
