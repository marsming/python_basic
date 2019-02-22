from flask import Flask

'''
#配置对象，里面定义需要给app添加的配置
class Config(object):
    DEBUG = True

#创建Flask类的对象，指向程序所在的包的名称
app = Flask(__name__)

#从配置对象中加载配置
app.config.from_object(Config)

@app.route('/')
def hello_world():
    return 'Hello World!'
'''

#创建Flask类的对象
app = Flask(__name__)

#从配置文件中加载配置
##app.config.from_pyfile('config.ini')

app.config.from_envvar('FLASKCONFIG')

@app.route('/')
def hello_word():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
