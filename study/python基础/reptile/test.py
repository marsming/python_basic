import requests
import re

getcodelist = __import__("股票代码")

code_url = "http://quote.eastmoney.com/stocklist.html"

codeList = getcodelist.urlTolist(code_url)
year_list = [2016,2017,2018,2019]
season = 1
for code in codeList:

			data_url = "http://quotes.money.163.com/trade/lsjysj_"+str(code)+".html?year="+'2018'+"&season="+'1'+'"'
			html = requests.get(data_url).text
			pat = """<tr.*class.*>.*<td.*>(.*?)</td>
					.*<td.*>(.*?)</td>
					.*<td.*>(.*?)</td>
					.*<td.*>(.*?)</td>
					.*<td.*>(.*?)</td>
					.*<td.*>(.*?)</td>
					.*<td.*>(.*?)</td>
					.*<td.*>(.*?)</td>
					.*<td.*>(.*?)</td>
					.*<td.*>(.*?)</td>
					.*<td.*>(.*?)</td>.*</tr>"""
			data = re.compile(pat).findall(html)
			print(data)


"""<tr.*class.*>.*<td.*>(.*?)</td>
.*<td.*>(.*?)</td>
.*<td.*>(.*?)</td>
.*<td.*>(.*?)</td>
.*<td.*>(.*?)</td>
.*<td.*>(.*?)</td>
.*<td.*>(.*?)</td>
.*<td.*>(.*?)</td>
.*<td.*>(.*?)</td>
.*<td.*>(.*?)</td>
.*<td.*>(.*?)</td>.*</tr>"""