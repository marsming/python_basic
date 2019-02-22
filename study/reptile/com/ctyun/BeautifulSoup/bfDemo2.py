from bs4 import BeautifulSoup

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <dir class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ur>
    </div>
</div>
'''

soup = BeautifulSoup(html,'lxml')
print("=======find_all(name,attrs,recursive,text,**kwargs)========")
print("=======name========")
print(soup.find_all("ul"))
print(type(soup.find_all("ul")))

for ul in soup.find_all('ul'):
    print(ul.find_all('li'))
print("=======attrs========")
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))
print("=======text========")
print(soup.find_all(text='Foo'))
print("=======find(name,attrs,recursive,text,**lwargs)========")
print(soup.find('ul'))
print(soup.find_all('ul'))
print(soup.find('page'))
