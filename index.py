from flask import Flask, render_template, request, redirect, url_for
import pickle
import os
from logging import getLogger, INFO, DEBUG
logger = getLogger(__name__)
logger.setLevel(INFO)
if os.environ.get('DEBUG', None):
    logger.setLevel(DEBUG)

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

# テキスト編集画面
@app.route('/editpage')
def edit():
    with open('test.data', 'rb') as datafile:
        data = pickle.load(datafile)
    return render_template('edit.html', filetext=data[0]["text"])

# テキスト登録
@app.route('/regist', methods=['POST'])
def regist():
    t = request.form['edittext']
    print(t)
    obj = [{"text":t}]
    with open('test.data', 'wb') as datafile:
        pickle.dump(obj, datafile)
        datafile.close()
    return redirect(url_for('edit'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
