#类
print('====================创建类和方法==========================')
class MyClass:
    i = 12345
    def hello(self):
        return 'hello world!'

#实例化类
x = MyClass

#访问类的属性和方法：
print('MyClass 类的属性 i 为：', x.i)
print('MyClass 类的方法 hello 为：', x.hello(0))


class pepole:
    #定义基本属性
    name = 'Mars'
    age = 20
    #定义私有属性,私有属性在类外部无法直接进行访问
    _weight = 0
    #定义构造方法：
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self._weight=w
    def speak(self):
        print('%s 说：我 %d 岁。' % (self.name,self.age))

#实例化类
p = pepole('Tom',10,30)
p.speak()

print('====================继承==========================')

class student(pepole):
    grade = ''

    def __init__(self, n, a, w, g):
        super().__init__(n, a, w)
        self.grade=g

    #重写父类的方法：
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

s = student('Jack',10,60,3)
s.speak()