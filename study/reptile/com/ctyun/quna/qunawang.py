import requests,re

def getList():
    place = input("请输入想搜索的区域、类型（如北京、热门景点等）：")
    sigthlist = []
    i = 1
    while i:
        url = "http://piao.qunar.com/ticket/list.htm?keyword="+place+"&page="+str(i)
        page = requests.get(url).text
        area = 'sight_item_detail.*?data-click-type="l_title".?>(.*?)</a>.*?'  #景区名称
        area_leve = 'class="level">(.*?)</span>.*?'    #景区级别
        area_add = 'class="area">.*?<a.*?>(.*?)</a>.*?'     #所在区域
        area_hot = 'class="product_star_level">.*?<em.*?title="(.*?)">.*?'      #热度
        address = 'class="address.*?>.*?<span.*?>(.*?)</span>.*?'       #地址
        intro = 'class="intro.*?>(.*?)</div>.*?'      #标语
        price = 'sight_item_price">.*?<em>(.*?)</em>.*?'    #起步价
        message = 'sight_item_do.*?href="(.*?)".*?'
        hot_num = 'sight_item_sold-num">.*?<span.*?>(.*?)</span>.*?'        #月销量
        pattern = area+area_leve+area_add+area_hot+address+intro+price+message+hot_num
        print(pattern)

getList()