from flask import Flask

app = Flask(__name__)

#指定访问路径位demo1
@app.route('/demo1')
def demo1():
    return 'demo1'

if __name__ == '__main__':
    app.run()
