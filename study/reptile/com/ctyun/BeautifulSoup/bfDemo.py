from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
<a href="http://example.com/title" class="sister" id="link3">Title</a>;
and they lived at the botton of a well.</p>
<p class="story">...123
'''

soup = BeautifulSoup(html,'lxml')
print("======基本使用=======")
print(soup.prettify())
print(soup.title.string)
print("=======选择元素======")
print(type(soup))
print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.p)
print("=======获取标签名称======")
print(soup.title.name)
print("=======获取标签属性======")
print(soup.p.attrs['name'])
print(soup.p['name'])
print(soup.a['href'])
print("=======获取标签内容======")
print(soup.p.string)
print(soup.a.string)
print("=======嵌套选择======")
print(soup.head.title.string)
print("=======子节点和子孙节点======")
print(soup.p.contents)
print(soup.body.contents)

print(soup.p.children)
for i,child in enumerate(soup.p.children):
    print(i,child)

print(soup.p.descendants)
for i,child in enumerate(soup.p.descendants):
    print(i,child)
