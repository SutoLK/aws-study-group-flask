"""
AI人生設計勉強会二日目
FlaskによるAPIの作成
"""

from flask import Flask, jsonify, request


# インスタンスの作成
# Javaのインスタンスと同じ考え方っぽい。Flaskがclassみたいなイメージ
app = Flask(__name__)


# どんなURLが来たらこれを実行するかを宣言
# jsonifyで渡したデータをブラウザで見ると順番が逆になっている(keyとvalueはそのまま)
@app.route('/')
def home():
    return jsonify({'message':'Hello', 'item':'apple', 'aaa':'bbb'})

# URLの指定と関数は一対一の関係になっている
# URLからデータを変数型で受け取ることもできる
@app.route('/item/<name>')
def get_item(name):
    return name


# POST形式の書き方

items = []

# postで送られてきたデータを配列に格納する関数
# get_json()を使うことでデータをdict型で扱うことができる

@app.route('/item', methods=['POST'])
def make_something():
    item = request.get_json()
    items.append(item)
    return jsonify(item)


# サーバの起動
if __name__ == '__main__':
    app.run()