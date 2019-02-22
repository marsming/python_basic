import requests,re
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

req = requests.get("http://blog.hexun.com/",headers=headers).text
#print(req)

pattern = '<li>.*?L">.*?<a.*?href="(.*?)".*?</a>.*?</li>'
urllist = set(re.compile(pattern).findall(req))
#print(urllist)

for i in urllist:
    #print(i)
    reqs = requests.get(i, headers=headers).text
    #print(reqs)
    soup = BeautifulSoup(reqs, "lxml")
    divlist = soup.select('.Article')
    #print(len())
    for j in divlist:
        #print(j)
        #print(j.select('div')[0])
        url = j.select('.ArticleTitle')[0].select('a')[0].get('href')
        title = j.select('.ArticleTitle')[0].select('a')[0].text
        click = j.select('.ArticleInfo')[0]
        print(url,title,click)
    break