from flask import Flask, render_template

app = Flask(__name__)

# 単純に書いたものを表示させる
@app.route('/')
def index():
    return 'hello'

# CSSやJavaScriptの外部ファイルを読み込む
@app.route('/extend')
def extend():
    return render_template('extend.html')
# テンプレートの内容を表示する
@app.route('/template')
def template():
    return render_template('index.html')

# テンプレートに値を渡してはめ込んで表示する
@app.route('/jinja')
def jinja():
    s = "title string"
    l = ["list 1", "list 2", "list 3"]
    d = {"name": "taro", "age": 20}
    b = True

    return render_template('jinja.html', s=s, l=l, d=d, b=b)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
