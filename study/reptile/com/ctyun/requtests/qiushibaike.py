import requests,re

#添加headers
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}


for i in range(1,14):
    req = requests.get("https://www.qiushibaike.com/text/",headers=headers).text
    pattern = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
    alltext = re.compile(pattern,re.S).findall(req)
    for j in range(1,len(alltext)):
        tatol = "第"+str(i)+"页第"+str(j)+"个段子的内容是："
        file = open('duanzi.txt', 'a',encoding="utf-8")
        data = tatol+"\n"+alltext[j]
        file.write(data)