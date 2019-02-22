import urllib.request
import re

#使用urllib爬取新闻网站
data = urllib.request.urlopen("http://news.sina.com.cn").read()
data_decode = data.decode("utf-8", "ignore")

pattern = 'href="(http://news.sina.com.cn/.*?)"'
allUrl = re.compile(pattern).findall(data_decode)

for i in range(0,len(allUrl)):
    try:
        print("第"+str(i)+"次爬取")
        thisurl = allUrl[i]
        file = "./sina_news/sina_news"+str(i)+".html"
        urllib.request.urlretrieve(thisurl,file)
        print("-------成功--------")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)