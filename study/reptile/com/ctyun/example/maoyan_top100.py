import re,requests
import json
from requests.exceptions import RequestException
'''
爬取猫眼电影榜单中TOP100中的信息
电影的num、名称、主演、上映时间、评分、图片链接等
'''

#添加请求头
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}

#发送请求
def get_one_page(url):
	try:
		response = requests.get(url,headers=headers)
		if response.status_code == 200:
			return response.text
		#return None
	except RequestException:
		return "无法获取页面"

#通过正则表达式获取想要信息
def parse_one_page(html):
	pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?'
						 'data-src="(.*?)@.*?>.*?'
						 'movie-item-info.*?name.*?<a.*?>(.*?)</a>.*?'
						 'star.*?>(.*?)</p>.*?'
						 'releasetime.*?>(.*?)</p>.*?'
						 'integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)
	items = re.findall(pattern, html)
	for item in items:
		yield {
			'number': item[0],
			'image': item[1],
			'title': item[2],
			'actor': item[3].strip(),
			'time': item[4].strip(),
			'score': item[5] + item[6]
		}


def write_to_file(context):
	file = open('result.json', 'a', encoding='utf-8')
	file.write(json.dumps(context)+'\n')
	file.close()


if __name__ == '__main__':
	for page in range(10):
		url = 'https://maoyan.com/board/4?offset='+str(page*10)
		html = get_one_page(url)

		for item in parse_one_page(html):
			print(item)
			write_to_file(item)




