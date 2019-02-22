import requests
from requests.exceptions import RequestException
from pyquery import PyQuery as pq

'''
爬取东方财富股票代码
'''
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}

def get_page(url):
	response = requests.get(url, headers=headers)
	try:
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return '网页无法打开'

if __name__ == '__main__':
	url = 'http://quote.eastmoney.com/stocklist.html'
	#html = get_page(url)
	doc = pq(url).html()
	print(doc)


