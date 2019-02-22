import re

import requests

'''
    <div.*?info.*?>
    .*?<a.*?>(.*?)</a>
    .*?<div.*?meta-info.*?>.*?author.*?>(.*?)</a>
    <time>(.*?)</time></div>
    .*?counts.*?>.*?read-count.*?>(.*?)</span>
    .*?</div>
'''

url = "https://read.douban.com/essays/"
response = requests.get(url)
print(response.status_code)
html = response.text

pattern = re.compile('''
    <div.*?info.*?>
    .*?<a.*?>(.*?)</a>
    .*?<div.*?meta-info.*?>.*?author.*?>(.*?)</a>
    .*?<time>(.*?)</time></div>
    .*?</div>
    ''', re.S)
items = re.findall(pattern, html)
type(items)
