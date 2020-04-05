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

# 401エラー
@app.errorhandler(401)
def unauthorized(error):
    return render_template('401.html'), 401

# 404エラー
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# 500エラー
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

# 503エラー
@app.errorhandler(503)
def service_unavilable(error):
    return render_template('503.html'), 503

# CSSやJavaScriptの外部ファイルを読み込む
@app.route('/extend')
def extend():
    return render_template('extend.html')
# テンプレートの内容を表示する
@app.route('/template')
def template():
    return render_template('index.html')

# テンプレートに値を渡してはめ込んで表示する
@app.route('/jinja2')
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

# リダイレクト
@app.route('/redirect')
def redirect_jinja():
    return redirect(url_for('jinja2'))

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

# フロント用サンプル
@app.route('/html5')
def html5():
    return render_template('html5.html')



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
