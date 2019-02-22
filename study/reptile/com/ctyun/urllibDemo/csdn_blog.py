from urllib import request,error
import re

#爬取csdn博文
headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")
opener = request.build_opener()
opener.addheaders=[headers]
request.install_opener(opener)
url = 'http://blog.csdn.net/'
data = request.urlopen(url).read().decode("utf-8", "ignore")

pattern = 'data-track-click.*?"mod":"popu_459","con":",(.*?),.*?>'
allurl = re.compile(pattern).findall(data)
#print(allurl)
for i in range(0,len(allurl)):
    try:
        print("第"+str(i)+"次爬取")
        file = "./csdn_blog/csdn_blog_"+str(i)+".html"
        request.urlretrieve(allurl[i],filename=file)
        print("------成功-------")
    except error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)


