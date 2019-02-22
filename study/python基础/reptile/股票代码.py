"""
爬取股票代码及股票历史交易数据
"""
import requests
import re


def urlTolist(url):
	global allCodeList
	html = requests.get(url).text
	pattern = '<li>.*?<a.*?target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'
	code = re.compile(pattern=pattern).findall(html)
	allCodeList = []
	for item in code:
		# print(item)
		if item[0] == '6' or item[0] == '0' or item[0] == '3':
			allCodeList.append(item)
		else:
			pass
	return allCodeList
