import urllib.request

#使用西刺代理http://www.xicidaili.com/

def use_proxy(url,proxy_addr):
    #设置代理
    proxy = urllib.request.ProxyHandler({"http":proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    #将opener安装为全局
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    return data

proxy_addr="118.116.41.24:8118"
url="http://www.baidu.com"
data = use_proxy(url, proxy_addr)
print(len(data))